"""
activity clazz views

:author: gexuewen
:date: 2020/01/03
"""
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from activity.constant.code import CLAZZ_ALREADY_IN
from activity.models import Activity, ActivityClazz
from activity.serializers import ActivityClazzSerializer
from clazz.models import Clazz
from util import result_util


class ActivityClazzViewSet(ListModelMixin,
                           CreateModelMixin,
                           GenericAPIView):
    """
    activity clazz view set

    :author: gexuewen
    :date: 2020/01/03
    """

    def __init__(self):
        super(ActivityClazzViewSet, self).__init__()
        self.activity = None
        self.clazz = None

    def get_queryset(self):
        activity_id = self.request.query_params.get('activity_id')
        return ActivityClazz.objects.filter(activity_id=activity_id)

    serializer_class = ActivityClazzSerializer

    def get(self, request):
        """
        get activity clazz

        :author: gexuewen
        :date: 2020/01/03
        """
        res = self.list(self, request)
        data = res.data
        data_iter = map(lambda ac: {
            'id': ac.get('id'),
            'clazz': ac.get('clazz')
        }, data)
        data = list(data_iter)
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
