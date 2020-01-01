"""
activity views

:author: gexuewen
:date: 2019/12/28
"""
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

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


class AddActivity(GenericAPIView, CreateModelMixin):
    """
    activity list view

    :author: gexuewen
    :date: 2020/01/01
    """
    serializer_class = ActivitySerializer

    def post(self, request):
        """
        post handler

        :author: gexuewen
        :date: 2020/01/01
        """
        return self.create(request)


# class DeleteActivity(GenericAPIView, DestroyModelMixin):
#     """
#     activity list view
#
#     :author: gexuewen
#     :date: 2020/01/01
#     """
#     serializer_class = ActivitySerializer
#     queryset = Activity.objects.all()
#     lookup_field = 'id'
#
#     def delete(self, request, id):
#         return self.destroy(request)
#
#     def perform_destroy(self, instance):
#         instance.state = 1
#         instance.save()
