# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-05 20:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0029_grupos_subgrupos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupos',
            name='Clase',
        ),
        migrations.RemoveField(
            model_name='subgrupos',
            name='Grupo',
        ),
        migrations.DeleteModel(
            name='Grupos',
        ),
        migrations.DeleteModel(
            name='SubGrupos',
        ),
    ]
