"""
activity serializers

:author: gexuewen
:date: 2020/01/01
"""
from rest_framework.serializers import ModelSerializer

from activity.models import Activity, ActivityStudent, ActivityClazz
from clazz.serializers import ClazzSerializer
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
    """
    activity student serializer

    :author: gexuewen
    :date: 2020/01/02
    """
    activity = ActivitySerializer(many=False, read_only=True)
    student = StudentSerializer(many=False, read_only=True)

    class Meta:
        model = ActivityStudent
        fields = '__all__'

    def create(self, validated_data):
        return ActivityStudent.objects.create(activity=self.context["activity"],
                                              student=self.context['student'],
                                              **validated_data)


class ActivityClazzSerializer(ModelSerializer):
    """
    activity clazz serializer

    :author: gexuewen
    :date: 2020/01/03
    """
    activity = ActivitySerializer(many=False, read_only=True)
    clazz = ClazzSerializer(many=False, read_only=True)

    class Meta:
        model = ActivityClazz
        fields = '__all__'

    def create(self, validated_data):
        return ActivityStudent.objects.create(activity=self.context["activity"],
                                              clazz=self.context['clazz'],
                                              **validated_data)
