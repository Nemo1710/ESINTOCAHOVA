# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-22 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0013_productobodega'),
    ]

    operations = [
        migrations.AddField(
            model_name='pec',
            name='CHECK_D',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='pec',
            name='CHECK_LD',
            field=models.NullBooleanField(),
        ),
    ]
