from rest_framework.serializers import ModelSerializer

from core.models import Genero, Filme, Artista

class GeneroSerializer(ModelSerializer):
    class Meta:
        model = Genero
        fields = "__all__"

class FilmeSerializer(ModelSerializer):
    class Meta:
        model = Filme
        fields = "__all__"

class ArtistaSerializer(ModelSerializer):
    class Meta:
        model = Artista
        fields = "__all__"