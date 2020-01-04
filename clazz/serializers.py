"""
clazz serializers

:author: gexuewen
:date: 2020/01/03
"""
from rest_framework.serializers import ModelSerializer

from clazz.models import Clazz
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
