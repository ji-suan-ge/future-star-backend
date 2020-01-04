"""
clazz views

:author: gexuewen
:date: 2020/01/04
"""
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from clazz.constant.clazz_state import UNOPENED
from clazz.serializers import ClazzSerializer
from semester.models import Semester
from util import result_util


class ClazzViewSet(ListModelMixin,
                   CreateModelMixin,
                   GenericAPIView):
    """
    clazz view set

    :author: gexuewen
    :date: 2020/01/04
    """
    serializer_class = ClazzSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.semester = None

    def post(self, request):
        """
        create clazz

        :author: gexuewen
        :date: 2020/01/04
        """
        data = request.data.copy()
        semester_id = data.get('semester_id')
        self.semester = Semester.objects.filter(id=semester_id).first()
        data.update({'state': UNOPENED})
        clazz_serializer = self.get_serializer(data=data)
        clazz_serializer.is_valid(raise_exception=True)
        clazz_serializer.save()
        return result_util.success(clazz_serializer.data)

    def get_serializer_context(self):
        context = super(ClazzViewSet, self).get_serializer_context()
        context['semester'] = self.semester
        return context
