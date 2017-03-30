from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.


class DataModel(models.Model):
    gateway = models.ForeignKey(Gateway)
    node = models.ForeignKey(Node)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User)
    value = models.CharField()


class ErrorModel(models.Model):
    type = models.CharField()
    errorCode = models.IntegerField()


class Gateway(models.Model):
    gps_lat = models.FloatField()
    gps_lon = models.FloatField()
    last_seen = models.CharField()
    mac = models.CharField()
    serial = models.CharField()
    user = models.ForeignKey(User)


class Node(models.Model):
    app_eui = models.CharField()
    app_key = models.CharField()
    dev_addr = models.CharField()
    dev_eui = models.CharField()
    last_gateway = models.ForeignKey(Gateway)
    last_seen = models.DateTimeField()
    name = models.CharField()
    type = models.CharField()
    user = models.ForeignKey(User)


class Swarm(models.Model):
    created = models.DateTimeField()
    last_seen = models.DateTimeField()
    name = models.CharField()
    nodes = ArrayField(models.ForeignKey(Node))
    user = models.ForeignKey(User)


class User(models.Model):
    company = models.CharField()
    email = models.CharField()
    first_name = models.CharField()
    gateways = ArrayField(models.ForeignKey(Gateway))
    last_name = models.CharField()
    nodes = ArrayField(models.ForeignKey(Node))
    registered = models.CharField()
