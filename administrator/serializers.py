"""
serializers

:author: lishanZheng
:date: 2019/12/31
"""
from rest_framework import serializers
from .models import Administrator


class AdministratorSerializer(serializers.ModelSerializer):
    """
    administrator serializer

    :author: lishanZheng
    :date: 2019/12/28
    """
    class Meta:
        model = Administrator
        fields = '__all__'
