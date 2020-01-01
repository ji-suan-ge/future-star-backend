"""
views

:author: lishanZheng
:date: 2019/12/28
"""
from django.db.models import Q
from rest_framework import generics
from rest_framework import mixins

from student.constant.state import VALID, NOT_GRADUATE
from student.models import Student
from student.serializers import StudentSerializer
from util import result_util
from util.pagination import CustomPageNumberPagination


class StudentList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    administrator view set

    :author: lishanZheng
    :date: 2020/01/01
    """
    queryset = Student.objects.filter(Q(state=NOT_GRADUATE) | Q(state=VALID))
    serializer_class = StudentSerializer
    pagination_class = CustomPageNumberPagination

    def get(self, request):
        """
        get administrator list

        :author: lishanZheng
        :date: 2020/01/01
        """
        page = self.list(request).data
        return result_util.success(page)
