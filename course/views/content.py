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
    serializer_class = ContentSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = Content.objects.all()
        course_id = self.request.GET.get('course_id')
        if course_id is not None:
            queryset = Content.objects.filter(course_id__in=course_id)
        return queryset

    def post(self, request):
        """
        add content

        :author: lishanZheng
        :date: 2020/01/04
        """
        res = self.create(request)
        return result_util.success(res.data)

    def get(self, request):
        """
        get content list

        :author: lishanZheng
        :date: 2020/01/04
        """
        page = self.list(request).data
        return result_util.success(page)
