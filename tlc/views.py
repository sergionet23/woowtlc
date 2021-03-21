from rest_framework import viewsets

from .serializers import HeroSerializer, ConductorSerializer
from .models import Hero, Conductor


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer



#class ConductorViewSet(viewsets.ModeViewSet):
#    queryset = Conductor.objects.all().order_by('idconductor')
#    serializer_class = ConductorSerializer
