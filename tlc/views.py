from rest_framework import viewsets
from rest_framework import permissions
from .serializers import HeroSerializer, ConductorSerializer, OperadorSerializer
from .models import Hero, Conductor, Operador


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all().order_by('idconductor')
    serializer_class = ConductorSerializer
    permission_classes = [permissions.IsAuthenticated]


class OperadorViewSet(viewsets.ModelViewSet):
    queryset = Operador.objects.all().order_by('ci_operador')
    serializer_class = OperadorSerializer
    permission_classes = [permissions.IsAuthenticated]