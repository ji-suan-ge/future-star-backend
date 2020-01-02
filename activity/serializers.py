"""
activity serializers

:author: gexuewen
:date: 2020/01/01
"""
from rest_framework.serializers import ModelSerializer
from activity.models import Activity, ActivityStudent
from student.serializers import StudentSerializer


class ActivitySerializer(ModelSerializer):
    """
    activity serializer

    :author: gexuewen
    :date: 2020/01/01
    """

    class Meta:
        model = Activity
        fields = '__all__'


class ActivityStudentSerializer(ModelSerializer):
    student = StudentSerializer(many=False, read_only=True)
    activity = ActivitySerializer(many=False, read_only=True)

    class Meta:
        model = ActivityStudent
        fields = '__all__'
