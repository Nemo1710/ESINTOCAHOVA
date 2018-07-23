# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-14 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodegas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ORGANIZATION_CODE', models.CharField(max_length=5)),
                ('SEGMENT1', models.CharField(max_length=15)),
                ('ANTERIOR', models.CharField(max_length=15)),
                ('DESCRIPTION', models.TextField(max_length=200)),
                ('ATTRIBUTE3', models.CharField(blank=True, max_length=200, null=True)),
                ('ATTRIBUTE4', models.CharField(blank=True, max_length=200, null=True)),
                ('CANTIDAD', models.CharField(blank=True, max_length=10, null=True)),
                ('PRIMARY_UOM_CODE', models.CharField(max_length=5)),
                ('LOCALIZADOR', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ORGANIZATION_CODE', models.CharField(max_length=5)),
                ('SEGMENT1', models.CharField(max_length=11)),
                ('CATALOGACION', models.CharField(blank=True, max_length=200, null=True)),
                ('CLASE', models.CharField(blank=True, max_length=200, null=True)),
                ('DESCRIPTION', models.TextField(max_length=200)),
                ('MARCA', models.TextField(max_length=200)),
                ('LONG_DESCRIPTION', models.TextField(max_length=400)),
                ('ITEM_TYPE', models.TextField(max_length=10)),
                ('PRIMARY_UOM_CODE', models.CharField(max_length=5)),
                ('SECONDARY_UOM_CODE', models.CharField(blank=True, max_length=5, null=True)),
                ('SECONDARY_DEFAULT_IND', models.CharField(blank=True, max_length=5, null=True)),
                ('ATTRIBUTE_CATEGORY', models.CharField(blank=True, max_length=10, null=True)),
                ('ATTRIBUTE1', models.CharField(blank=True, max_length=5, null=True)),
                ('ATTRIBUTE2', models.CharField(blank=True, max_length=200, null=True)),
                ('GRUPO', models.CharField(blank=True, max_length=10, null=True)),
                ('ATTRIBUTE3', models.CharField(blank=True, max_length=200, null=True)),
                ('ATTRIBUTE4', models.CharField(blank=True, max_length=200, null=True)),
                ('ATTRIBUTE5', models.CharField(blank=True, max_length=200, null=True)),
                ('ATTRIBUTE6', models.CharField(blank=True, max_length=200, null=True)),
                ('ATTRIBUTE7', models.CharField(blank=True, max_length=200, null=True)),
                ('ATTRIBUTE8', models.CharField(blank=True, max_length=200, null=True)),
                ('ATTRIBUTE9', models.CharField(blank=True, max_length=200, null=True)),
                ('SUBGRUPO', models.CharField(blank=True, max_length=100, null=True)),
                ('ARTICULO', models.CharField(blank=True, max_length=100, null=True)),
                ('ATTRIBUTE11', models.CharField(blank=True, max_length=200, null=True)),
                ('ATTRIBUTE12', models.CharField(blank=True, max_length=200, null=True)),
                ('ATTRIBUTE13', models.CharField(blank=True, max_length=200, null=True)),
                ('ATTRIBUTE14', models.CharField(blank=True, max_length=200, null=True)),
                ('ATTRIBUTE15', models.CharField(blank=True, max_length=200, null=True)),
                ('GLOBAL_ATTRIBUTE8', models.CharField(blank=True, max_length=200, null=True)),
                ('GLOBAL_ATTRIBUTE1', models.CharField(blank=True, max_length=200, null=True)),
                ('GLOBAL_ATTRIBUTE2', models.CharField(blank=True, max_length=200, null=True)),
                ('GLOBAL_ATTRIBUTE3', models.CharField(blank=True, max_length=200, null=True)),
                ('GLOBAL_ATTRIBUTE4', models.CharField(blank=True, max_length=200, null=True)),
                ('GLOBAL_ATTRIBUTE5', models.CharField(blank=True, max_length=200, null=True)),
                ('SHELF_LIFE_DAYS', models.IntegerField(blank=True, null=True)),
                ('TEST_INTERVAL', models.CharField(blank=True, max_length=200, null=True)),
                ('EXPIRATION_ACTION_INTERVAL', models.CharField(blank=True, max_length=200, null=True)),
                ('EXPIRATION_ACTION_CODE', models.CharField(blank=True, max_length=200, null=True)),
                ('MATURITY_DAYS', models.CharField(blank=True, max_length=200, null=True)),
                ('HOLD_DAYS', models.CharField(blank=True, max_length=200, null=True)),
                ('SERIAL_NUMBER_CONTROL_CODE', models.CharField(blank=True, max_length=200, null=True)),
                ('AUTO_SERIAL_ALPHA_PREFIX', models.CharField(blank=True, max_length=200, null=True)),
                ('START_AUTO_SERIAL_NUMBER', models.CharField(blank=True, max_length=200, null=True)),
                ('LOCATION_CONTROL_CODE', models.CharField(blank=True, max_length=200, null=True)),
                ('RESTRICT_SUBINVENTORIES_CODE', models.CharField(blank=True, max_length=200, null=True)),
                ('RESTRICT_LOCATORS_CODE', models.CharField(blank=True, max_length=200, null=True)),
                ('LOT_STATUS_ENABLED', models.CharField(blank=True, max_length=200, null=True)),
                ('DEFAULT_LOT_STATUS_ID', models.CharField(blank=True, max_length=200, null=True)),
                ('COSTOVENTAS', models.CharField(blank=True, max_length=200, null=True)),
                ('BUYER_ID', models.CharField(blank=True, max_length=200, null=True)),
                ('LIST_PRICE_PER_UNIT', models.CharField(blank=True, max_length=200, null=True)),
                ('GASTOS', models.CharField(blank=True, max_length=200, null=True)),
                ('COMPROMISO', models.CharField(blank=True, max_length=200, null=True)),
                ('WEIGHT_UOM_CODE', models.CharField(blank=True, max_length=200, null=True)),
                ('CODIGO', models.CharField(blank=True, max_length=200, null=True)),
                ('VOLUME_UOM_CODE', models.CharField(blank=True, max_length=200, null=True)),
                ('UNIT_VOLUME', models.CharField(blank=True, max_length=200, null=True)),
                ('UNIT_LENGTH', models.CharField(blank=True, max_length=200, null=True)),
                ('UNIT_WIDTH', models.CharField(blank=True, max_length=200, null=True)),
                ('UNIT_HEIGHT', models.CharField(blank=True, max_length=200, null=True)),
                ('INVENTORY_PLANNING_CODE', models.CharField(blank=True, max_length=200, null=True)),
                ('PLANNER_CODE', models.CharField(blank=True, max_length=200, null=True)),
                ('PLANNING_MAKE_BUY_CODE', models.CharField(blank=True, max_length=200, null=True)),
                ('MIN_MINMAX_QUANTITY', models.CharField(blank=True, max_length=200, null=True)),
                ('MAX_MINMAX_QUANTITY', models.CharField(blank=True, max_length=200, null=True)),
                ('MINIMUM_ORDER_QUANTITY', models.CharField(blank=True, max_length=200, null=True)),
                ('MAXIMUM_ORDER_QUANTITY', models.CharField(blank=True, max_length=200, null=True)),
                ('FIXED_ORDER_QUANTITY', models.CharField(blank=True, max_length=200, null=True)),
                ('FIXED_DAYS_SUPPLY', models.CharField(blank=True, max_length=200, null=True)),
                ('FIXED_LOT_MULTIPLIER', models.CharField(blank=True, max_length=200, null=True)),
                ('SOURCE_TYPE', models.CharField(blank=True, max_length=200, null=True)),
                ('MRP_PLANNING_CODE', models.CharField(blank=True, max_length=200, null=True)),
                ('TAX_CODE', models.CharField(blank=True, max_length=200, null=True)),
                ('VENTAS', models.CharField(blank=True, max_length=200, null=True)),
                ('PROCESS_YIELD_SUBINVENTORY', models.CharField(blank=True, max_length=200, null=True)),
                ('SEGMENT1_1', models.CharField(blank=True, max_length=200, null=True)),
                ('SEGMENT2', models.CharField(blank=True, max_length=200, null=True)),
                ('SEGMENT3', models.CharField(blank=True, max_length=200, null=True)),
                ('SEGMENT4', models.CharField(blank=True, max_length=200, null=True)),
                ('SEGMENT5', models.CharField(blank=True, max_length=200, null=True)),
                ('SO_TRANSACTIONS_FLAG', models.CharField(blank=True, max_length=200, null=True)),
                ('TAXABLE_FLAG', models.CharField(blank=True, max_length=200, null=True)),
                ('PURCHASING_TAX_CODE', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
