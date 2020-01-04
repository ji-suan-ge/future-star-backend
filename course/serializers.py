"""
activity serializers

:author: gexuewen
:date: 2020/01/01
"""
from rest_framework.serializers import ModelSerializer

from course.models import Resource, Teacher, Content


class ResourceSerializer(ModelSerializer):
    """
    resource serializer

    :author: lishanZheng
    :date: 2020/01/03
    """

    class Meta:
        model = Resource
        fields = '__all__'


class TeacherSerializer(ModelSerializer):
    """
    teacher serializer

    :author: lishanZheng
    :date: 2020/01/04
    """

    class Meta:
        model = Teacher
        fields = '__all__'


class ContentSerializer(ModelSerializer):
    """
    content serializer

    :author: lishanZheng
    :date: 2020/01/04
    """

    class Meta:
        model = Content
        fields = '__all__'
