from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Item(models.Model):
    access_token = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Conductor(models.Model):
    idconductor = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    mail = models.EmailField(max_length=50)
    estado = models.BooleanField


class Operador(models.Model):
    ci_operador = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    mail = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    estado = models.BooleanField
    tipo_operador = models.CharField(max_length=20)
    id_lugar_asignado = models.IntegerField()
    hora_inicio_trabajo = models.IntegerField()
    Hora_fin_trabajo = models.IntegerField()
    calificacion_promedio = models.IntegerField()


class LugaresDeTrabajo(models.Model):
    id_Lugar_asignado = models.AutoField(primary_key=True)
    nombre_ubicacion = models.CharField(max_length=50)
    cantidad_total_lugares = models.IntegerField(max_length=3)
    ubicacion = models.CharField(max_length=50)
    latidud = models.FloatField
    longitud = models.FloatField
    cantidad_restante_lugares = models.IntegerField(max_length=3)


class Propinas(models.Model):
    id_transaccion = models.AutoField(primary_key=True)
    monto = models.IntegerField
    fecha = models.DateTimeField


class Denuncia(models.Model):
    id_transaccion = models.AutoField(primary_key=True)
    tipo_denuncia = models.IntegerField
    texto_denuncia = models.CharField(max_length=50)
    fecha = models.DateTimeField


class TipoDenuncia(models.Model):
    id_tipo_denuncia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)


class Comercio(models.Model):
    id_comercio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    texto = models.CharField(max_length=250)
    imagen = models.ImageField
    direccion = models.CharField(max_length=50)
    latitud = models.FloatField
    longitud = models.FloatField


class Servicios(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    id_comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)


class OcuparLugar(models.Model):
    id_transaccion = models.AutoField(primary_key=True)
    id_conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    ci_operado = models.ForeignKey(Operador, on_delete=models.CASCADE)
    id_Lugar_asignado = models.ForeignKey(LugaresDeTrabajo, on_delete=models.CASCADE)
    fecha_hora_inicio = models.DateTimeField
    fecha_hora_fin = models.DateTimeField


class Calificaciones(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    id_transaccion = models.ForeignKey(OcuparLugar, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=40)


def __str__(self):
    return self.name
