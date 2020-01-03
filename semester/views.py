"""
views

:author: lishanZheng
:date: 2019/12/28
"""
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from semester.models import Semester
from semester.serializers import SemesterSerializer
from util import result_util
from util.pagination import CustomPageNumberPagination


class SemesterViewSet(ListModelMixin,
                      CreateModelMixin,
                      GenericAPIView):
    """
    semester view set

    :author: lishanZheng
    :date: 2020/01/02
    """
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    pagination_class = CustomPageNumberPagination

    def post(self, request):
        """
        create semester

        :author: lishanZheng
        :date: 2020/01/02
        """
        res = self.create(request)
        return result_util.success(res.data)

    def get(self, request):
        """
        get semester list

        :author: lishanZheng
        :date: 2020/01/03
        """
        res = self.list(request)
        return result_util.success(res.data)
