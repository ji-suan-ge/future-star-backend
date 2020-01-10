"""
activity clazz views

:author: gexuewen
:date: 2020/01/03
"""
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from activity.constant.code import CLAZZ_ALREADY_IN
from activity.models import Activity, ActivityClazz
from activity.serializers import ActivityClazzSerializer
from clazz.models import Clazz
from util import result_util
from util.pagination import CustomPageNumberPagination


class ActivityClazzViewSet(ListModelMixin,
                           CreateModelMixin,
                           GenericAPIView):
    """
    activity clazz view set

    :author: gexuewen
    :date: 2020/01/03
    """
    pagination_class = CustomPageNumberPagination
    serializer_class = ActivityClazzSerializer

    def __init__(self):
        super(ActivityClazzViewSet, self).__init__()
        self.activity = None
        self.clazz = None

    def get_queryset(self):
        activity_id = self.request.query_params.get('activity_id')
        return ActivityClazz.objects.filter(activity_id=activity_id)

    def get(self, request):
        """
        get activity clazz

        :author: gexuewen
        :date: 2020/01/03
        """
        res = self.list(request)
        data = res.data
        results = data.get('results')
        target_results = list(map(lambda result: result.get('clazz'), results))
        data = {
            'count': data.get('count'),
            'results': target_results
        }
        return result_util.success(data)

    def post(self, request):
        """
        create activity clazz

        :author: gexuewen
        :date: 2020/01/03
        """
        activity_id = request.data.get('activity_id')
        clazz_id = request.data.get('clazz_id')
        self.activity = Activity.objects.filter(id=activity_id).first()
        self.clazz = Clazz.objects.filter(id=clazz_id).first()
        activity_clazz = ActivityClazz.objects.filter(activity_id=activity_id,
                                                      clazz_id=clazz_id)
        if activity_clazz.count() > 0:
            return result_util.error(CLAZZ_ALREADY_IN, '此班级已经在活动列表中')
        data = {
            'activity_id': activity_id,
            'clazz_id': clazz_id
        }
        activity_clazz = ActivityClazz.objects.create(**data)
        activity_clazz_serializer = self.get_serializer(instance=activity_clazz)
        return result_util.success(activity_clazz_serializer.data)

    def get_serializer_context(self):
        context = super(ActivityClazzViewSet, self).get_serializer_context()
        context['activity'] = self.activity
        context['clazz'] = self.clazz
        return context


class ActivityClazzDetailViewSet(generics.GenericAPIView):
    """
    activity clazz detail view set

    :author: gexuewen
    :date: 2020/01/10
    """

    def delete(self, request, activity_id, param):
        """
        update clazz

        :author: gexuewen
        :date: 2020/01/04
        """
        if param == 'all':
            activity_clazz_list = ActivityClazz.objects.filter(activity_id=activity_id)
            for activity_clazz in activity_clazz_list:
                activity_clazz.delete()
            return result_util.success_empty()
        if not self:
            pass
        return result_util.success_empty()
