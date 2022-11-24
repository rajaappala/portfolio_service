from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from equity.models import Script
from equity.models import ScriptDetail

class ScriptSerializer(ModelSerializer):
    class Meta:
        model = Script
        fields = '__all__'

    def create(self, validated_data):
        return Script.objects.create(**validated_data)


class ScriptDetailSerializer(ModelSerializer):
    class Meta:
        model = ScriptDetail
        fields = '__all__'

    def create(self, validated_data):
        return ScriptDetail.objects.create(**validated_data)