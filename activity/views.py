"""
activity views

:author: gexuewen
:date: 2019/12/28
"""
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin

from util import result_util
from util.pagination import CustomPageNumberPagination
from activity.models import Activity
from activity.serializers import ActivitySerializer


class ActivityViewSet(ListModelMixin,
                      CreateModelMixin,
                      GenericAPIView):
    """
    activity view set

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
        res = self.list(request)
        return result_util.success(res.data)

    def post(self, request):
        """
        create activity

        :author: gexuewen
        :date: 2020/01/01
        """
        res = self.create(request)
        return result_util.success(res.data)


class ActivityDetailViewSet(UpdateModelMixin,
                            GenericAPIView):
    """
    activity detail view set

    :author: gexuewen
    :date: 2020/01/02
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'primary_key'

    def put(self, request, primary_key):
        """
        update activity

        :author: gexuewen
        :date: 2020/01/02
        """
        res = self.partial_update(request, primary_key)
        return result_util.success(res.data)

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
