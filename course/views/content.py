"""
content

:author: lishanZheng
:date: 2020/01/04
"""
from rest_framework import mixins, generics

from course.models import Content
from course.serializers import ContentSerializer
from util import result_util
from util.pagination import CustomPageNumberPagination


class ContentViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    """
    content view set

    :author: lishanZheng
    :date: 2020/01/04
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    pagination_class = CustomPageNumberPagination

    def post(self, request):
        """
        add content

        :author: lishanZheng
        :date: 2020/01/04
        """
        res = self.create(request)
        return result_util.success(res.data)
