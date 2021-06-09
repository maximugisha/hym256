from rest_framework import serializers

from .models import Language, Hymn, Ad, HymnNumber, HymnFile


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class HymnSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hymn
        fields = '__all__'


class HymnNumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HymnNumber
        fields = '__all__'


class HymnFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HymnFile
        fields = '__all__'


class AdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
