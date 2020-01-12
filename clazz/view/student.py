"""
clazz student views

:author: gexuewen
:date: 2020/01/08
"""
from rest_framework import mixins, generics

from clazz.constant import clazz_student_state
from clazz.constant.clazz_student_state import WAIT_FOR_AUDIT
from clazz.constant.code import ALREADY_APPLY, INVALID_STUDENT_FORM
from clazz.models import Clazz, ClazzStudent
from clazz.serializers import ClazzStudentSerializer
from student.constant import student_state
from student.models import Evaluation, Student, ApplicationInformation, RecommendationPeople
from util import result_util
from util.dictionary import remove_key
from util.pagination import CustomPageNumberPagination


class ClazzStudentViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          generics.GenericAPIView):
    """
    clazz student view set

    :author: gexuewen
    :date: 2020/01/08
    """
    serializer_class = ClazzStudentSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        query_set = ClazzStudent.objects.all()
        params = self.request.query_params
        clazz_id = params.get('clazz_id')
        if clazz_id:
            query_set = query_set.filter(clazz_id=clazz_id)
        clazz_student_state_data = params.get('clazz_student_state')
        if clazz_student_state_data:
            query_set = query_set.filter(state=clazz_student_state_data)
        student_id = params.get('student_id')
        if student_id:
            query_set = query_set.filter(student_id=student_id)
        return query_set

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.clazz = None
        self.student = None
        self.apply = None
        self.evaluation = None

    def get(self, request):
        """
        get clazz student

        :author: gexuewen
        :date: 2020/01/09
        """
        res = self.list(request).data
        return result_util.success(res)

    def post(self, request):
        """
        create clazz student

        :author: gexuewen
        :date: 2020/01/08
        """
        data = request.data.copy()
        student_id = data.get('student_id')
        clazz_id = data.get('clazz_id')
        recommendation_peoples = data.get('recommendation_people')
        clazz_student = ClazzStudent.objects.filter(clazz_id=clazz_id, student_id=student_id)
        if clazz_student.count() > 0:
            return result_util.error(ALREADY_APPLY, '已经参加过')
        self.evaluation = Evaluation.objects.create()
        apply_data = data.get('application')
        self.apply = ApplicationInformation.objects.create(**apply_data)
        if recommendation_peoples:
            for recommendation_people in recommendation_peoples:
                RecommendationPeople.objects.create(information=self.apply, **recommendation_people)
        self.student = Student.objects.filter(id=student_id).first()
        self.clazz = Clazz.objects.filter(id=clazz_id).first()
        data.update({'state': WAIT_FOR_AUDIT})
        clazz_student_serializer = self.get_serializer(data=data)
        if clazz_student_serializer.is_valid():
            clazz_student_serializer.save()
        else:
            return result_util.error(INVALID_STUDENT_FORM, '请求表单错误')
        self.clazz.current_people_number = self.clazz.current_people_number + 1
        self.clazz.save()
        return result_util.success_empty()

    def get_serializer_context(self):
        context = super(ClazzStudentViewSet, self).get_serializer_context()
        context['clazz'] = self.clazz
        context['student'] = self.student
        context['apply'] = self.apply
        context['evaluation'] = self.evaluation
        return context


class ClazzStudentDetailViewSet(mixins.UpdateModelMixin,
                                generics.GenericAPIView):
    """
    clazz student detail view set

    :author: gexuewen
    :date: 2020/01/10
    """
    queryset = ClazzStudent.objects.filter()
    serializer_class = ClazzStudentSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'primary_key'

    def put(self, request, primary_key):
        """
        update clazz student

        :author: gexuewen
        :date: 2020/01/10
        """
        data = request.data
        clazz_student = self.get_object()
        state = data.get('state')
        if state:
            clazz_student.state = state
            clazz_student.save()
            if state == clazz_student_state.GRADUATED:
                student = clazz_student.student
                student.state = student_state.VALID
                student.save()
            else:
                return result_util.error(INVALID_STUDENT_FORM, '表单内容错误')
        evaluation_data = data.get('evaluation')
        if evaluation_data:
            evaluation = clazz_student.evaluation
            evaluation.fraction = evaluation_data.get('fraction')
            evaluation.description = evaluation_data.get('description')
            evaluation.save()
        if not primary_key:
            # make pylint happy
            print(primary_key)
        clazz_student_serializer = ClazzStudentSerializer(clazz_student)
        data = clazz_student_serializer.data.copy()
        data = remove_key(data, 'clazz')
        data = remove_key(data, 'student')
        data = remove_key(data, 'apply')
        return result_util.success(data)
