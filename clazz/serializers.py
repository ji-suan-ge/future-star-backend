"""
clazz serializers

:author: gexuewen
:date: 2020/01/03
"""
from rest_framework.serializers import ModelSerializer

import student.serializers as student_serializer
from clazz.models import Clazz, ClazzStudent
from semester.serializers import SemesterSerializer


class ClazzSerializer(ModelSerializer):
    """
    clazz serializer

    :author: gexuewen
    :date: 2020/01/03
    """
    semester = SemesterSerializer(many=False, read_only=True)

    class Meta:
        model = Clazz
        fields = '__all__'

    def create(self, validated_data):
        return Clazz.objects.create(
            semester=self.context["semester"],
            **validated_data)


class ClazzStudentSerializer(ModelSerializer):
    """
    clazz student serializer

    :author: gexuewen
    :date: 2020/01/08
    """
    clazz = ClazzSerializer(many=False, read_only=True)
    student = student_serializer.StudentSerializer(many=False, read_only=True)
    apply = student_serializer.ApplicationInformationSerializer(many=False, read_only=True)
    evaluation = student_serializer.EvaluationSerializer(many=False, read_only=True)

    class Meta:
        model = ClazzStudent
        fields = '__all__'

    def create(self, validated_data):
        return ClazzStudent.objects.create(
            clazz=self.context["clazz"],
            student=self.context["student"],
            apply=self.context["apply"],
            evaluation=self.context["evaluation"],
            **validated_data)
