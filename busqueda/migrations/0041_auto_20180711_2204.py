# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-11 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0040_sgrupo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sgrupo',
            name='Grupo',
        ),
        migrations.AddField(
            model_name='sgrupo',
            name='Clases',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='busqueda.Clases'),
        ),
        migrations.AddField(
            model_name='sgrupo',
            name='Grupos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='busqueda.Grupos'),
        ),
    ]
