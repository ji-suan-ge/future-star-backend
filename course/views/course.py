"""
course

:author: lishanZheng
:date: 2020/01/04
"""
from rest_framework import mixins, generics

from course.models import Course, Teacher
from course.serializers import CourseSerializer
from util import result_util
from util.pagination import CustomPageNumberPagination


class CourseViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    """
    course view set

    :author: lishanZheng
    :date: 2020/01/04
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CustomPageNumberPagination

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.teacher = None

    def post(self, request):
        """
        add course

        :author: lishanZheng
        :date: 2020/01/04
        """
        teacher_data = request.data.get('teacher')
        self.teacher = Teacher.objects.create(**teacher_data)
        course = self.get_serializer(data=request.data)
        if course.is_valid():
            course.save()
        return result_util.success(course.data)

    def get_serializer_context(self):
        context = super(CourseViewSet, self).get_serializer_context()
        context['teacher'] = self.teacher
        return context


class CourseDetailViewSet(mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.GenericAPIView):
    """
    course detail view set

    :author: lishanZheng
    :date: 2020/01/05
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'primary_key'

    def put(self, request, primary_key):
        """
        update course

        :author: lishanZheng
        :date: 2020/01/05
        """
        result_course = self.partial_update(request, primary_key)
        return result_util.success(result_course.data)
