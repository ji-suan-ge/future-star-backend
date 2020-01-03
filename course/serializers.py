"""
activity serializers

:author: gexuewen
:date: 2020/01/01
"""
from rest_framework.serializers import ModelSerializer

from course.models import Resource


class ResourceSerializer(ModelSerializer):
    """
    resource serializer

    :author: lishanZheng
    :date: 2020/01/03
    """

    class Meta:
        model = Resource
        fields = '__all__'
