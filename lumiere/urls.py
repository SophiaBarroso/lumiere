from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import GeneroViewSet, FilmeViewSet, ArtistaViewSet

router = DefaultRouter()
router.register(r'genero', GeneroViewSet)
router.register(r'filme', FilmeViewSet)
router.register(r'artista', ArtistaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]