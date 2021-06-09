from rest_framework import viewsets

from .serializers import LanguageSerializer, HymnSerializer, AdSerializer
from .models import Language, Hymn, Ad


# Create your views here.

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all().order_by('name')
    serializer_class = LanguageSerializer


class HymnViewSet(viewsets.ModelViewSet):
    queryset = Hymn.objects.all().order_by('name')
    serializer_class = HymnSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all().order_by('name')
    serializer_class = AdSerializer
