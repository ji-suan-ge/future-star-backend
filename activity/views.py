"""
activity views

:author: gexuewen
:date: 2019/12/28
"""
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from util import result_util
from util.pagination import CustomPageNumberPagination
from activity.models import Activity
from activity.serializers import ActivitySerializer


class ActivityList(GenericAPIView, ListModelMixin):
    """
    activity list view

    :author: gexuewen
    :date: 2020/01/01
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    pagination_class = CustomPageNumberPagination

    def get(self, request):
        """
        get activity list

        :author: gexuewen
        :date: 2020/01/01
        """
        page = self.list(request).data
        return result_util.success(page)
