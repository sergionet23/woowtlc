from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Item(models.Model):
    access_token = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)


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


def __str__(self):
    return self.name
