# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-19 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0005_auto_20180619_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='SHELF_LIFE_DAYS',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
