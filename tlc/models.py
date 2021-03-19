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
    idconductor = models.IntegerField
    usr = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    mail = models.EmailField(max_length=40)
    status = models.BooleanField



def __str__(self):
    return self.name