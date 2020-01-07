"""
student views

:author: gexuewen
:date: 2020/01/02
"""
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from activity.constant.activity_student_state import WAIT_FOR_PAY
from activity.constant.code import ALREADY_JOIN
from activity.models import ActivityStudent, Activity
from activity.serializers import ActivityStudentSerializer
from student.models import Student
from util import result_util
from util.pagination import CustomPageNumberPagination


class ActivityStudentViewSet(ListModelMixin,
                             CreateModelMixin,
                             GenericAPIView):
    """
    activity student view set

    :author: gexuewen
    :date: 2020/01/02
    """

    def __init__(self):
        super(ActivityStudentViewSet, self).__init__()
        self.activity = None
        self.student = None

    serializer_class = ActivityStudentSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        activity_id = self.request.query_params.get('activity_id')
        queryset = ActivityStudent.objects.filter(activity_id=activity_id)
        return queryset

    def get(self, request):
        """
        get activity student list

        :author: gexuewen
        :date: 2020/01/02
        """
        data = self.list(request).data
        target_results = map(lambda result: result.get('student'), data.get('results'))
        data = {
            'count': data.get('count'),
            'results': list(target_results)
        }
        return result_util.success(data)

    def post(self, request):
        """
        create activity student

        :author: gexuewen
        :date: 2020/01/03
        """
        activity_id = request.data.get('activity_id')
        student_id = request.data.get('student_id')
        self.activity = Activity.objects.filter(id=activity_id).first()
        self.student = Student.objects.filter(id=student_id).first()
        activity_student = ActivityStudent.objects.filter(activity_id=activity_id,
                                                          student_id=student_id)
        if activity_student.count() > 0:
            return result_util.error(ALREADY_JOIN, '已经参加过')
        data = {
            'state': WAIT_FOR_PAY
        }
        activity_student_serializer = self.get_serializer(data=data)
        if activity_student_serializer.is_valid():
            activity_student_serializer.save()
        return result_util.success(activity_student_serializer.data)

    def get_serializer_context(self):
        context = super(ActivityStudentViewSet, self).get_serializer_context()
        context['activity'] = self.activity
        context['student'] = self.student
        return context
