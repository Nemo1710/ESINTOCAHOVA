# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-11 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0002_auto_20180611_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='CATALOGACION',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='productos',
            name='CLASE',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]