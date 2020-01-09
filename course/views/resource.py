"""
resource

:author: lishanZheng
:date: 2020/01/04
"""
from rest_framework import mixins, generics

from course.models import Resource
from course.serializers import ResourceSerializer
from util import result_util
from util.pagination import CustomPageNumberPagination


class ResourceViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    """
    resource view set

    :author: lishanZheng
    :date: 2020/01/03
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    pagination_class = CustomPageNumberPagination

    def post(self, request):
        """
        add resource

        :author: lishanZheng
        :date: 2020/01/03
        """
        res = self.create(request)
        return result_util.success(res.data)


class ResourceDetailViewSet(mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    """
    resource detail views set

    :author: lishanZheng
    :date: 2020/01/04
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'primary_key'

    def put(self, request, primary_key):
        """
        update resource

        :author: lishanZheng
        :date: 2020/01/04
        """
        result = self.partial_update(request, primary_key)
        return result_util.success(result.data)
