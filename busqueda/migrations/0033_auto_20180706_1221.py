# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0032_auto_20180706_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupos',
            name='Clase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busqueda.Clases'),
        ),
    ]
