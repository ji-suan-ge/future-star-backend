"""
course

:author: lishanZheng
:date: 2020/01/04
"""
from rest_framework import mixins, generics

from course.models import Course, Teacher
from course.serializers import CourseSerializer
from course.test.generate.teacher import get_default_teacher_data
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

    def post(self, request):
        """
        add course

        :author: lishanZheng
        :date: 2020/01/04
        """
        teacher_data = get_default_teacher_data()
        teacher = Teacher(**teacher_data)
        teacher.save()
        course = CourseSerializer(data=request.data, context={'teacher': teacher})
        if course.is_valid():
            course.save()
        return result_util.success(course.data)
