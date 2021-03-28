from rest_framework import serializers

from .models import Conductor, Operador, LugaresDeTrabajo, Propinas, Denuncia, TipoDenuncia


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
