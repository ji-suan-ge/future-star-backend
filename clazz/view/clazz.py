"""
clazz views

:author: gexuewen
:date: 2020/01/04
"""
from rest_framework import mixins, generics

from clazz.constant.clazz_state import UNOPENED
from clazz.constant.code import INVALID_CLAZZ_FORM
from clazz.models import Clazz, ClazzStudent
from clazz.serializers import ClazzSerializer
from semester.models import Semester
from util import result_util
from util.dictionary import remove_key
from util.pagination import CustomPageNumberPagination


class ClazzViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    """
    clazz view set

    :author: gexuewen
    :date: 2020/01/04
    """
    serializer_class = ClazzSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        query_set = Clazz.objects.all()
        params = self.request.query_params
        clazz_state = params.get('clazz_state')
        if clazz_state:
            query_set = query_set.filter(state=clazz_state)
        semester_id = params.get('semester_id')
        if semester_id:
            query_set = query_set.filter(semester_id=semester_id)
        student_id = self.request.query_params.get('student_id')
        if student_id:
            clazz_student_set = ClazzStudent.objects.filter(student_id=student_id)
            clazz_id_list = list(clazz_student_set.values_list('clazz_id', flat=True))
            query_set = query_set.filter(id__in=clazz_id_list)
        return query_set

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.semester = None

    def get(self, request):
        """
        get clazz

        :author: gexuewen
        :date: 2020/01/04
        """
        res = self.list(request)
        data = res.data
        target_results = map(lambda result: remove_key(result, 'semester'), data.get('results'))
        result_data = {
            'count': data.get('count'),
            'results': list(target_results)
        }
        return result_util.success(result_data)

    def post(self, request):
        """
        create clazz

        :author: gexuewen
        :date: 2020/01/04
        """
        data = request.data.copy()
        semester_id = data.get('semester_id')
        self.semester = Semester.objects.filter(id=semester_id).first()
        data.update({'state': UNOPENED})
        clazz_serializer = self.get_serializer(data=data)
        if clazz_serializer.is_valid():
            clazz_serializer.save()
        else:
            return result_util.error(INVALID_CLAZZ_FORM, '请求表单内容错误')
        return result_util.success(clazz_serializer.data)

    def get_serializer_context(self):
        context = super(ClazzViewSet, self).get_serializer_context()
        context['semester'] = self.semester
        return context


class ClazzDetailViewSet(mixins.UpdateModelMixin,
                         generics.GenericAPIView):
    """
    clazz detail view set

    :author: gexuewen
    :date: 2020/01/04
    """
    queryset = Clazz.objects.filter()
    serializer_class = ClazzSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'primary_key'

    def put(self, request, primary_key):
        """
        update clazz

        :author: gexuewen
        :date: 2020/01/04
        """
        semester_id = request.data.get('semester_id')
        semester = Semester.objects.filter(id=semester_id).first()
        if semester is not None:
            clazz = self.get_object()
            clazz.semester = semester
            clazz.save()
        res = self.partial_update(request, primary_key)
        return result_util.success(res.data)
