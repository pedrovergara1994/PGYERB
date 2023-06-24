from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Instrumento(models.Model):
    name = models.TextField(max_length=100)
    desc = models.TextField(max_length=200)
    precio = models.IntegerField(null=True, blank=True)
    img = models.TextField( null=True, blank=True)


class Cliente(models.Model):
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150)
    rut = models.CharField(max_length=11)
    phone = models.CharField(max_length=12, null=True, blank=True)
    mail = models.EmailField(max_length=254, null=True, blank=True)
    password = models.CharField(max_length=500, null=True, blank=True)
    create_date = models.DateTimeField(default=timezone.now)


class Carrito(models.Model):
    cliente_id = models.IntegerField(null=True, blank=True)
    instrumentos = models.JSONField(null=True, blank=True)
    total = models.IntegerField(default=0)
    created_date = models.DateTimeField(
        default=timezone.now)


class Compra(models.Model):
    cliente_id = models.IntegerField(null=True, blank=True)
    instrumentos = models.JSONField(null=True, blank=True)
    total = models.IntegerField(default=0)
    created_date = models.DateTimeField(
        default=timezone.now)
