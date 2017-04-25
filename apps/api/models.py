from django.contrib.postgres.fields import ArrayField
from django.db import models
from rest_framework import serializers

# Create your models here.

class User(models.Model):
    company = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    gateways = models.ForeignKey('Gateway', null=False)
    last_name = models.CharField(max_length=100)
    nodes = models.ForeignKey('Node', null=False)
    registered = models.CharField(max_length=100)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class Gateway(models.Model):
    gps_lat = models.FloatField()
    gps_lon = models.FloatField()
    last_seen = models.CharField(max_length=100)
    mac = models.CharField(max_length=100)
    serial = models.CharField(max_length=100)

class Node(models.Model):
    app_eui = models.CharField(max_length=100)
    app_key = models.CharField(max_length=100)
    dev_addr = models.CharField(max_length=100)
    dev_eui = models.CharField(max_length=100)
    last_gateway = models.ForeignKey(Gateway)
    last_seen = models.DateTimeField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class DataModel(models.Model):
    gateway = models.ForeignKey(Gateway)
    node = models.ForeignKey(Node)
    timestamp = models.DateTimeField()
    value = models.CharField(max_length=100)


class Swarm(models.Model):
    created = models.DateTimeField()
    last_seen = models.DateTimeField()
    name = models.CharField(max_length=100)
    nodes = models.ForeignKey(Node)


class ErrorModel(models.Model):
    type = models.CharField(max_length=100)
    errorCode = models.IntegerField()
