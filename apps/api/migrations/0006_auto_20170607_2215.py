# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20170607_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gateway',
            name='last_seen',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='node',
            name='last_seen',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]