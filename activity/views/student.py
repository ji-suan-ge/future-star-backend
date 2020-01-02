"""
student views

:author: gexuewen
:date: 2020/01/02
"""
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from activity.models import ActivityStudent
from activity.serializers import ActivityStudentSerializer
from util import result_util
from util.pagination import CustomPageNumberPagination


class ActivityStudentViewSet(ListModelMixin,
                             CreateModelMixin,
                             GenericAPIView):
    """
    activity student view set

    :author: gexuewen
    :date: 2020/01/02
    """
    serializer_class = ActivityStudentSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        activity_id = self.request.query_params.get('activity_id')
        queryset = ActivityStudent.objects.filter(activity_id=activity_id)
        return queryset

    def get(self, request):
        """
        get activity student list

        :author: gexuewen
        :date: 2020/01/02
        """
        page = self.list(request).data
        return result_util.success(page)
