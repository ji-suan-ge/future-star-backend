"""
serializers

:author: lishanZheng
:date: 2019/12/31
"""
from rest_framework import serializers
from .models import Administrator, Privilege


class PrivilegeSerializer(serializers.ModelSerializer):
    """
    administrator serializer

    :author: lishanZheng
    :date: 2019/12/28
    """
    class Meta:
        model = Privilege
        fields = '__all__'


class AdministratorSerializer(serializers.ModelSerializer):
    """
    administrator serializer

    :author: lishanZheng
    :date: 2019/12/28
    """
    privilege = PrivilegeSerializer(many=False, read_only=True)

    class Meta:
        model = Administrator
        fields = '__all__'

    def create(self, validated_data):
        return Administrator.objects.create(
            privilege=self.context["privilege"],
            **validated_data)
