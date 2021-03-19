from rest_framework import serializers

from .models import Hero , Conductor


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name','alias')


class ConductorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conductor
        filter = ('idconductor', 'usr','password','nombre', 'apellido','telefono','mail','status' )
