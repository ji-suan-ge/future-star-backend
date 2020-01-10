"""
views

:author: lishanZheng
:date: 2019/12/28
"""
from rest_framework import mixins, generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from clazz.constant import clazz_state
from clazz.models import Clazz
from semester.constant.code import CLAZZ_NOT_CLOSE
from semester.constant.semester_state import CLOSED
from semester.models import Semester
from semester.serializers import SemesterSerializer
from util import result_util
from util.pagination import CustomPageNumberPagination


class SemesterViewSet(ListModelMixin,
                      CreateModelMixin,
                      GenericAPIView):
    """
    semester view set

    :author: lishanZheng
    :date: 2020/01/02
    """
    query_set = Semester.objects.all()
    queryset = query_set.order_by('-period_semester')
    serializer_class = SemesterSerializer
    pagination_class = CustomPageNumberPagination

    def post(self, request):
        """
        create semester

        :author: lishanZheng
        :date: 2020/01/02
        """
        res = self.create(request)
        return result_util.success(res.data)

    def get(self, request):
        """
        get semester list

        :author: lishanZheng
        :date: 2020/01/03
        """
        res = self.list(request)
        return result_util.success(res.data)


class SemesterDetailViewSet(mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    """
    semester detail view set

    :author: lishanZheng
    :date: 2020/01/03
    """
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'primary_key'

    def put(self, request, primary_key):
        """
        update semester

        :author: lishanZheng
        :date: 2020/01/03
        """
        key = primary_key
        state = request.data.get('state')
        if state is not None:
            state = int(state)
        if state == CLOSED:
            clazz_list = Clazz.objects.filter(semester_id=key)
            count = len(clazz_list)
            clazz_closed = Clazz.objects.filter(semester_id=key, state=clazz_state.CLOSED)
            count_closed = len(clazz_closed)
            if count != count_closed:
                return result_util.error(CLAZZ_NOT_CLOSE, '存在课程没有结束')
        res = self.partial_update(request, key)
        return result_util.success(res.data)
