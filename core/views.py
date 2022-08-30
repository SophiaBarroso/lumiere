from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from core.models import Artista, Filme, Genero
from core.serializers import GeneroSerializer, FilmeSerializer, ArtistaSerializer

class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class FilmeViewSet(ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

class ArtistaViewSet(ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
