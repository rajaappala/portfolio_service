from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from equity.models import Script
from equity.models import ScriptDetail

class ScriptSerializer(ModelSerializer):
    class Meta:
        model = Script
        fields = '__all__'

    def create(self, validated_data):
        return Script.objects.create(**validated_data)


class ScriptDetailSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ScriptDetail
        fields = '__all__'

    def create(self, validated_data):
        return ScriptDetail.objects.create(**validated_data)