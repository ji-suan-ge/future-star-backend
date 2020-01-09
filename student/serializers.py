"""
serializers

:author: lishanZheng
:date: 2020/01/01
"""
from rest_framework import serializers

from student.models import ApplicationInformation, Company, Evaluation
from student.models import RecommendationPeople, Student, WechatStudent


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
    recommendation_peoples = RecommendationPeopleSerializer(many=True, read_only=True)

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


class WechatStudentSerializer(serializers.ModelSerializer):
    """
    wechat student serializer

    :author: egxuewen
    :date: 2020/01/09
    """
    student = StudentSerializer(many=False, read_only=True)

    class Meta:
        model = WechatStudent
        fields = '__all__'

    def create(self, validated_data):
        return WechatStudent.objects.create(
            student=self.context["student"],
            **validated_data)
