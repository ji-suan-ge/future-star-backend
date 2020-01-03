"""
clazz serializers

:author: gexuewen
:date: 2020/01/03
"""
from rest_framework.serializers import ModelSerializer

from clazz.models import Clazz


class ClazzSerializer(ModelSerializer):
    """
    clazz serializer

    :author: gexuewen
    :date: 2020/01/03
    """
    class Meta:
        model = Clazz
        fields = '__all__'
