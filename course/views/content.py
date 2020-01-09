"""
content

:author: lishanZheng
:date: 2020/01/04
"""
from rest_framework import mixins, generics

from course.models import Content, Resource
from course.serializers import ContentSerializer, ResourceSerializer
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
        :date: 2020/01/09
        """
        course_id = self.request.GET.get('course_id')
        contents = Content.objects.filter(course__id=course_id)
        content_id = list(contents.values_list('id', flat=True))
        times_i = len(content_id)
        content_list = []
        for i in range(times_i):
            content = ContentSerializer(contents[i]).data
            resources = Resource.objects.filter(content_id=contents[i].id)
            times_j = len(resources)
            section = []
            for j in range(times_j):
                section.append(ResourceSerializer(resources[j]).data)
            content = {
                'id': contents[i].id,
                'content_name': contents[i].content_name,
                'resources': section
            }
            content_list.append(content)
            res = {
                'results': content_list
            }
        return result_util.success(res)


class ContentDetailViewSet(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    """
    content detail views set

    :author: lishanZheng
    :date: 2020/01/04
    """
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = 'primary_key'
    lookup_field = 'id'

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
        over = self.destroy(request, primary_key)
        if over is None:
            pass
        return result_util.success_empty()
