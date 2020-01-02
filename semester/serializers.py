"""
serializers

:author: lishanZheng
:date: 2020/01/01
"""
from rest_framework import serializers
from .models import Semester


class SemesterSerializer(serializers.ModelSerializer):
    """
    semester serializer

    :author: lishanZheng
    :date: 2020/01/02
    """

    class Meta:
        model = Semester
        fields = '__all__'
