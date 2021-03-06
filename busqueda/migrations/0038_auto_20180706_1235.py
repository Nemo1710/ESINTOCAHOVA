# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-06 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0037_grupos_subgrupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SGrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subgrupo', models.CharField(max_length=2)),
                ('Titulo', models.CharField(max_length=100)),
                ('Grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busqueda.Grupos')),
            ],
        ),
        migrations.RemoveField(
            model_name='subgrupo',
            name='Grupo',
        ),
        migrations.DeleteModel(
            name='SubGrupo',
        ),
    ]
