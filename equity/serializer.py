from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from equity.models import Script, ScriptDetail, Dividend, Bonus, Split

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


class DividendSerializer(ModelSerializer):
    class Meta:
        model = Dividend
        fields = '__all__'


class BonusSerializer(ModelSerializer):
    class Meta:
        model = Bonus
        fields = '__all__'


class SplitSerializer(ModelSerializer):
    class Meta:
        model = Split
        fields = '__all__'