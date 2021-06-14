from rest_framework import viewsets
from rest_framework import generics
from django_filters import rest_framework as filters

from .serializers import LanguageSerializer, HymnSerializer, AdSerializer, HymnNumberSerializer, HymnFileSerializer
from .models import Language, Hymn, Ad, HymnNumber, HymnFile


# Create your views here.

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all().order_by('name')
    serializer_class = LanguageSerializer


class HymnNumberViewSet(viewsets.ModelViewSet):
    queryset = HymnNumber.objects.all().order_by('number')
    serializer_class = HymnNumberSerializer

#--- Filter file by lyrics id ---#
class HymnFileFilter(filters.FilterSet):
    class Meta:
        model = HymnFile
        fields = {
            'lyrics' : ['exact'],
        }

class HymnFileViewSet(viewsets.ModelViewSet):
    queryset = HymnFile.objects.all().order_by('lyrics')
    serializer_class = HymnFileSerializer
    lookup_field = 'lyrics'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HymnFileFilter


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all().order_by('name')
    serializer_class = AdSerializer


#--- Filter hymns by language id ---#
class HymnFilter(filters.FilterSet):
    class Meta:
        model = Hymn
        fields = {
            'language' : ['exact'],
        }

class HymnViewSet(viewsets.ModelViewSet):
    queryset = Hymn.objects.all().order_by('title')
    serializer_class = HymnSerializer
    lookup_field = 'language'
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = HymnFilter

#class HymnViewSet(generics.ListCreateAPIView):
#    queryset = Hymn.objects.all()
#    serializer_class = HymnSerializer
#    lookup_field = 'language'
#    filter_backends = (filters.DjangoFilterBackend,)
#    filterset_class = HymnFilter