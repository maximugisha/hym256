from rest_framework import viewsets
from django.shortcuts import HttpResponse

from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

from .serializers import LanguageSerializer, HymnSerializer, AdSerializer, HymnNumberSerializer, HymnFileSerializer
from .models import Language, Hymn, Ad, HymnNumber, HymnFile


# Create your views here.

def index(request):
    return HttpResponse('Welcome to Tuyimbe App ')


class LanguageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Language.objects.all().order_by('name')
    serializer_class = LanguageSerializer


class HymnNumberViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = HymnNumber.objects.all().order_by('number')
    serializer_class = HymnNumberSerializer


class HymnFileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = HymnFile.objects.all().order_by('lyrics')
    serializer_class = HymnFileSerializer

class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all().order_by('name')
    serializer_class = AdSerializer


class HymnViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Hymn.objects.all()
    serializer_class = HymnSerializer
