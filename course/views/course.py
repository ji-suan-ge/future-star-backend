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
    serializer_class = CourseSerializer
    pagination_class = CustomPageNumberPagination

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.teacher = None

    def get_queryset(self):
        queryset = Course.objects.all()
        clazz_id = self.request.GET.get('clazz_id')
        state = self.request.GET.get('state')
        if clazz_id is not None:
            queryset = Course.objects.filter(clazz_id=clazz_id)
            if state is not None:
                queryset = Course.objects.filter(state=state, clazz_id=clazz_id)
        return queryset

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

    def get(self, request):
        """
        get course list

        :author: lishanZheng
        :date: 2020/01/05
        """
        result_course_list = self.list(self).data
        return result_util.success(result_course_list)

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
