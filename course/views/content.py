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


class ContentDetailViewSet(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    """
    content detail view set

    :author: lishanZheng
    :date: 2020/01/04
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'primary_key'

    def put(self, request, primary_key):
        """
        update content

        :author: lishanZheng
        :date: 2020/01/04
        """
        res = self.partial_update(request, primary_key)
        return result_util.success(res.data)

    def delete(self, request, primary_key):
        """
        delete content

        :author: lishanZheng
        :date: 2020/01/04
        """
        self.destroy(request, primary_key)
        return result_util.success_empty()
