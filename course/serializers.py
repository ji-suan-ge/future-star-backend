"""
activity serializers

:author: gexuewen
:date: 2020/01/01
"""
from rest_framework.serializers import ModelSerializer

from course.models import Resource, Teacher, Content, Course


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
    resources = ResourceSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    """
    course serializer

    :author: lishanZheng
    :date: 2020/01/04
    """
    teacher = TeacherSerializer(many=False, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        return Course.objects.create(
            teacher=self.context["teacher"],
            **validated_data)
