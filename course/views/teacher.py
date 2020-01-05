"""
resource

:author: lishanZheng
:date: 2020/01/04
"""
from rest_framework import mixins, generics

from course.models import Teacher
from course.serializers import TeacherSerializer
from util import result_util
from util.pagination import CustomPageNumberPagination


class TeacherViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    """
    teacher view set

    :author: lishanZheng
    :date: 2020/01/04
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pagination_class = CustomPageNumberPagination

    def post(self, request):
        """
        add teacher

        :author: lishanZheng
        :date: 2020/01/04
        """
        res = self.create(request)
        return result_util.success(res.data)


class TeacherDetailViewSet(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    """
    teacher detail view set

    :author: lishanZheng
    :date: 2020/01/05
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'primary_key'

    def put(self, request, primary_key):
        """
        update teacher

        :author: lishanZheng
        :date: 2020/01/04
        """
        res = self.update(request, primary_key)
        return result_util.success(res.data)
