from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *

# ConductorSerializer, OperadorSerializer, LugaresDeTrabajoSerializer, PropinasSerializer, DenunciaSerializer, TipoDenunciaSerializer

from .models import *

# Conductor, Operador, LugaresDeTrabajo, Propinas, Denuncia, TipoDenuncia


class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all().order_by('idconductor')
    serializer_class = ConductorSerializer
    permission_classes = [permissions.IsAuthenticated]


class OperadorViewSet(viewsets.ModelViewSet):
    queryset = Operador.objects.all().order_by('ci_operador')
    serializer_class = OperadorSerializer
    permission_classes = [permissions.IsAuthenticated]


class LugaresDeTrabajoViewSet(viewsets.ModelViewSet):
    queryset = LugaresDeTrabajo.objects.all().order_by('id_Lugar_asignado')
    serializer_class = LugaresDeTrabajoSerializer
    permission_classes = [permissions.IsAuthenticated]


class PropinasViewSet(viewsets.ModelViewSet):
    queryset = Propinas.objects.all().order_by('id_transaccion')
    serializer_class = PropinasSerializer
    permission_classes = [permissions.IsAuthenticated]


class DenunciaViewSet(viewsets.ModelViewSet):
    queryset = Denuncia.objects.all().order_by('id_transaccion')
    serializer_class = DenunciaSerializer
    permission_classes = [permissions.IsAuthenticated]


class TipoDenunciaViewSet(viewsets.ModelViewSet):
    queryset = TipoDenuncia.objects.all().order_by('id_tipo_denuncia')
    serializer_class = TipoDenunciaSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComercioViewSet(viewsets.ModelViewSet):
    queryset = Comercio.objects.all().order_by('id_comercio')
    serializer_class = Comercio
    permission_classes = [permissions.IsAuthenticated]


class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all().order_by('id_servicio')
    serializer_class = Servicios
    permission_classes = [permissions.IsAuthenticated]


class OcuparLugaresViewSet(viewsets.ModelViewSet):
    queryset = OcuparLugar.objects.all().order_by('id_transaccion')
    serializer_class = OcuparLugar
    permission_classes = [permissions.IsAuthenticated]


class CalificacionesViewSet(viewsets.ModelViewSet):
    queryset = Calificaciones.objects.all().order_by('id_calificacion')
    serializer_class = Calificaciones
    permission_classes = [permissions.IsAuthenticated]