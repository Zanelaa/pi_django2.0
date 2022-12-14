from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import AlimentoViewSet,CardapioViewSet,RefeicoesViewSet

router = DefaultRouter()
router.register(r'Alimentos', AlimentoViewSet)
router.register(r'Cardapios', CardapioViewSet)
router.register(r'Refeicoes', RefeicoesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]