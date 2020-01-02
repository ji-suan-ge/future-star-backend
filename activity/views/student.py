from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from activity.models import ActivityStudent
from activity.serializers import ActivityStudentSerializer
from util import result_util
from util.pagination import CustomPageNumberPagination


class StudentActivityViewSet(ListModelMixin,
                             CreateModelMixin,
                             GenericAPIView):
    serializer_class = ActivityStudentSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        print(self.request.query_params)
        queryset = ActivityStudent.objects.filter(activity_id=self.request.query_params.get('activity_id'))
        return queryset

    def get(self, request):
        page = self.list(request).data
        return result_util.success(page)
