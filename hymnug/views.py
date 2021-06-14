from rest_framework import viewsets

from .serializers import LanguageSerializer, HymnSerializer, AdSerializer, HymnNumberSerializer, HymnFileSerializer
from .models import Language, Hymn, Ad, HymnNumber, HymnFile


# Create your views here.

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all().order_by('name')
    serializer_class = LanguageSerializer


class HymnNumberViewSet(viewsets.ModelViewSet):
    queryset = HymnNumber.objects.all().order_by('number')
    serializer_class = HymnNumberSerializer


class HymnFileViewSet(viewsets.ModelViewSet):
    queryset = HymnFile.objects.all().order_by('lyrics')
    serializer_class = HymnFileSerializer


class HymnViewSet(viewsets.ModelViewSet):
    queryset = Hymn.objects.all().order_by('title')
    filterset_fields = ['language']
    serializer_class = HymnSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all().order_by('name')
    serializer_class = AdSerializer
