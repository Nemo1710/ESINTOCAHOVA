# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0010_auto_20180621_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodega',
            name='Articulos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bodega',
            name='Items',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
