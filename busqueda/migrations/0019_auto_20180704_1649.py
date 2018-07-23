# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-04 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0018_auto_20180704_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Clase', models.CharField(max_length=2)),
                ('Titulo', models.CharField(max_length=30)),
                ('Descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='bodega',
            name='Nombre',
            field=models.CharField(max_length=5),
        ),
    ]