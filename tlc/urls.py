from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'conductor', views.ConductorViewSet)
router.register(r'operador', views.OperadorViewSet)
router.register(r'lugares de trabajo', views.LugaresDeTrabajoViewSet)
router.register(r'propinas', views.PropinasViewSet)
router.register(r'denuncia', views.DenunciaViewSet)
router.register(r'tipo de denuncia', views.TipoDenunciaViewSet)
router.register(r'comercio', views.ComercioViewSet)
router.register(r'servicios', views.ServiciosViewSet)
router.register(r'ocupar lugares', views.OcuparLugaresViewSet)
router.register(r'Calificaiones', views.CalificacionesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]