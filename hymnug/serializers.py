from rest_framework import serializers

from .models import Language, Hymn, Ad, HymnNumber, HymnFile


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name', 'short_name', 'created', 'updated']


class HymnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hymn
        fields = ['id', 'hymn_number', 'language', 'title', 'lyrics', 'created', 'updated']


class HymnNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = HymnNumber
        fields = ['id', 'number', 'created', 'updated']


class HymnFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HymnFile
        fields = ['id', 'lyrics', 'url', 'created', 'updated']


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'name', 'url', 'image_url', 'created', 'updated', 'expired']
