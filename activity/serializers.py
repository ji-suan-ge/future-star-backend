"""
activity serializers

:author: gexuewen
:date: 2020/01/01
"""
from rest_framework.serializers import ModelSerializer

from activity.models import Activity


class ActivitySerializer(ModelSerializer):
    """
    activity serializer

    :author: gexuewen
    :date: 2020/01/01
    """
    class Meta:
        model = Activity
        fields = '__all__'
