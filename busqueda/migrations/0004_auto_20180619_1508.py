# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-19 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0003_auto_20180615_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='ATTRIBUTE1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='DESCRIPTION',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='productos',
            name='LONG_DESCRIPTION',
            field=models.TextField(max_length=500),
        ),
    ]
