from rest_framework import serializers

from .models import Conductor, Operador, LugaresDeTrabajo, Propinas, Denuncia, TipoDenuncia, Comercio, Servicios, OcuparLugar, Calificaciones


class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'


class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = '__all__'


class LugaresDeTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LugaresDeTrabajo
        fields = '__all__'


class PropinasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propinas
        fields = '__all__'


class DenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Denuncia
        fields = '__all__'


class TipoDenunciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDenuncia
        fields = '__all__'


class ComercioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comercio
        fields = '__all__'


class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = '__all__'


class OcuparLugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = OcuparLugar
        fields = '__all__'


class CalificacionesLugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificaciones
        fields = '__all__'
