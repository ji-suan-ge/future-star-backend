"""
resource

:author: lishanZheng
:date: 2020/01/04
"""
from rest_framework import mixins, generics

from course.models import Resource
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
    queryset = Resource.objects.all()
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
