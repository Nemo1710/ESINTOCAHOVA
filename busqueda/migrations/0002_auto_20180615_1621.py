# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-15 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodegas',
            name='ANTERIOR',
            field=models.CharField(max_length=65),
        ),
    ]