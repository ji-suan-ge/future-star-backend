"""
serializers

:author: lishanZheng
:date: 2020/01/01
"""
from rest_framework import serializers

from .models import Student, Evaluation, RecommendationPeople, ApplicationInformation, Company


class EvaluationSerializer(serializers.ModelSerializer):
    """
    evaluation serializer

    :author: lishanZheng
    :date: 2020/01/01
    """

    class Meta:
        model = Evaluation
        fields = '__all__'


class RecommendationPeopleSerializer(serializers.ModelSerializer):
    """
    recommendation people serializer

    :author: lishanZheng
    :date: 2019/12/28
    """

    class Meta:
        model = RecommendationPeople
        fields = '__all__'


class ApplicationInformationSerializer(serializers.ModelSerializer):
    """
    application information serializer

    :author: lishanZheng
    :date: 2019/12/28
    """

    class Meta:
        model = ApplicationInformation
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    """
    company serializer

    :author: lishanZheng
    :date: 2019/12/28
    """

    class Meta:
        model = Company
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    """
    student serializer

    :author: lishanZheng
    :date: 2020/01/01
    """
    company = CompanySerializer(many=False, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        return Company.objects.create(
            company=self.context["company"],
            **validated_data)
