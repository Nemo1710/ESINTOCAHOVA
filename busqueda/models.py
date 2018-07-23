# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms
#from smart_selects.db_fields import ChainedForeignKey







# Create your models here.
class Bodega(models.Model):
	Nombre = models.CharField(max_length=5)
	Provincia=models.CharField(max_length=70, blank=True, null=True)
	Telefono=models.CharField(max_length=70, blank=True, null=True)
	Localizacion = models.CharField(max_length=50, blank=True, null=True)
	Articulos = models.IntegerField(blank=True, null=True)
	Items = models.IntegerField(blank=True, null=True)


	def __unicode__(self):
		return str(self.Nombre)+" "+str(self.Localizacion)





class ConfUsuario(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bodega=models.ForeignKey(Bodega)


	def __unicode__(self):
		return str(self.user.username)

#dsad




#Vacia solo tiene los indices
class PEC(models.Model):
	SEGMENT1 = models.CharField(max_length=11,unique=True)
	CATALOGACION=models.CharField(max_length=200,blank=True, null=True)
	CLASE=models.CharField(max_length=2,blank=True, null=True)
	#GRUPO=models.CharField(max_length=2,blank=True, null=True)
	#SUBGRUPO = models.CharField(max_length=2, blank=True, null=True)
	DESCRIPTION = models.TextField(max_length=500,blank=True, null=True)
	CHECK_D = models.BooleanField()
	CHECK_LD = models.BooleanField()

	MARCA=models.TextField(max_length=200,blank=True, null=True)
	LONG_DESCRIPTION=models.TextField(max_length=500,blank=True, null=True)
	ITEM_TYPE=models.TextField(max_length=10,blank=True, null=True)
	PRIMARY_UOM_CODE=models.CharField(max_length=100,blank=True, null=True)
	SECONDARY_UOM_CODE=models.CharField(max_length=5,blank=True, null=True)
	SECONDARY_DEFAULT_IND=models.CharField(max_length=5,blank=True, null=True)
	ATTRIBUTE_CATEGORY=models.CharField(max_length=10,blank=True, null=True)
	ATTRIBUTE1=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE2=models.CharField(max_length=200,blank=True, null=True)
	GRUPO=models.CharField(max_length=10,blank=True, null=True)
	ATTRIBUTE3=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE4=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE5=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE6=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE7=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE8=models.CharField(max_length=200,blank=True, null=True)
	#ESPACIO EN BLANCO
	ATTRIBUTE9=models.CharField(max_length=500,blank=True, null=True)
	SUBGRUPO=models.CharField(max_length=100,blank=True, null=True)
	ARTICULO=models.CharField(max_length=100,blank=True, null=True)
	ATTRIBUTE11=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE12=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE13=models.CharField(max_length=200,blank=True, null=True)
	#ESPACIO EN BLANCO
	ATTRIBUTE14=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE15=models.CharField(max_length=200,blank=True, null=True)
	GLOBAL_ATTRIBUTE8=models.CharField(max_length=200,blank=True, null=True)
	GLOBAL_ATTRIBUTE1=models.CharField(max_length=200,blank=True, null=True)
	GLOBAL_ATTRIBUTE2=models.CharField(max_length=200,blank=True, null=True)
	GLOBAL_ATTRIBUTE3=models.CharField(max_length=200,blank=True, null=True)
	GLOBAL_ATTRIBUTE4=models.CharField(max_length=200,blank=True, null=True)
	GLOBAL_ATTRIBUTE5=models.CharField(max_length=200,blank=True, null=True)
	SHELF_LIFE_DAYS=models.CharField(max_length=200,blank=True, null=True)
	TEST_INTERVAL=models.CharField(max_length=200,blank=True, null=True)
	EXPIRATION_ACTION_INTERVAL=models.CharField(max_length=200,blank=True, null=True)
	EXPIRATION_ACTION_CODE=models.CharField(max_length=200,blank=True, null=True)
	MATURITY_DAYS=models.CharField(max_length=200,blank=True, null=True)
	HOLD_DAYS=models.CharField(max_length=200,blank=True, null=True)
	SERIAL_NUMBER_CONTROL_CODE=models.CharField(max_length=200,blank=True, null=True)
	AUTO_SERIAL_ALPHA_PREFIX=models.CharField(max_length=200,blank=True, null=True)
	START_AUTO_SERIAL_NUMBER=models.CharField(max_length=200,blank=True, null=True)
	LOCATION_CONTROL_CODE=models.CharField(max_length=200,blank=True, null=True)
	RESTRICT_SUBINVENTORIES_CODE=models.CharField(max_length=200,blank=True, null=True)
	RESTRICT_LOCATORS_CODE=models.CharField(max_length=200,blank=True, null=True)
	LOT_STATUS_ENABLED=models.CharField(max_length=200,blank=True, null=True)
	DEFAULT_LOT_STATUS_ID=models.CharField(max_length=200,blank=True, null=True)
	COSTOVENTAS=models.CharField(max_length=200,blank=True, null=True)
	BUYER_ID=models.CharField(max_length=200,blank=True, null=True)
	LIST_PRICE_PER_UNIT=models.CharField(max_length=200,blank=True, null=True)
	GASTOS=models.CharField(max_length=200,blank=True, null=True)
	COMPROMISO=models.CharField(max_length=200,blank=True, null=True)
	WEIGHT_UOM_CODE=models.CharField(max_length=200,blank=True, null=True)
	DIGITOSFINALES = models.CharField(max_length=3, blank=True, null=True)
	CODIGO=models.CharField(max_length=9,blank=True, null=True)
	VOLUME_UOM_CODE=models.CharField(max_length=200,blank=True, null=True)
	UNIT_VOLUME=models.CharField(max_length=200,blank=True, null=True)
	UNIT_LENGTH=models.CharField(max_length=200,blank=True, null=True)
	UNIT_WIDTH=models.CharField(max_length=200,blank=True, null=True)
	UNIT_HEIGHT=models.CharField(max_length=200,blank=True, null=True)
	INVENTORY_PLANNING_CODE=models.CharField(max_length=200,blank=True, null=True)
	PLANNER_CODE=models.CharField(max_length=200,blank=True, null=True)
	PLANNING_MAKE_BUY_CODE=models.CharField(max_length=200,blank=True, null=True)
	MIN_MINMAX_QUANTITY=models.CharField(max_length=200,blank=True, null=True)
	MAX_MINMAX_QUANTITY=models.CharField(max_length=200,blank=True, null=True)
	MINIMUM_ORDER_QUANTITY=models.CharField(max_length=200,blank=True, null=True)
	MAXIMUM_ORDER_QUANTITY=models.CharField(max_length=200,blank=True, null=True)
	FIXED_ORDER_QUANTITY=models.CharField(max_length=200,blank=True, null=True)
	FIXED_DAYS_SUPPLY=models.CharField(max_length=200,blank=True, null=True)
	FIXED_LOT_MULTIPLIER=models.CharField(max_length=200,blank=True, null=True)
	SOURCE_TYPE=models.CharField(max_length=200,blank=True, null=True)
	MRP_PLANNING_CODE=models.CharField(max_length=200,blank=True, null=True)
	TAX_CODE=models.CharField(max_length=200,blank=True, null=True)
	VENTAS=models.CharField(max_length=200,blank=True, null=True)
	PROCESS_YIELD_SUBINVENTORY=models.CharField(max_length=200,blank=True, null=True)
	SEGMENT1_1=models.CharField(max_length=200,blank=True, null=True)
	SEGMENT2=models.CharField(max_length=200,blank=True, null=True)
	SEGMENT3=models.CharField(max_length=200,blank=True, null=True)
	SEGMENT4=models.CharField(max_length=200,blank=True, null=True)
	SEGMENT5=models.CharField(max_length=200,blank=True, null=True)
	SO_TRANSACTIONS_FLAG=models.CharField(max_length=200,blank=True, null=True)
	TAXABLE_FLAG=models.CharField(max_length=200,blank=True, null=True)
	PURCHASING_TAX_CODE=models.CharField(max_length=200,blank=True, null=True)

	def __unicode__(self):
		return str(self.SEGMENT1)


#DataTotal.xlsx
class Productos(models.Model):
	ORGANIZATION_CODE = models.CharField(max_length=5)
	SEGMENT1 = models.CharField(max_length=11)
	CATALOGACION=models.CharField(max_length=200,blank=True, null=True)
	CLASE=models.CharField(max_length=200,blank=True, null=True)
	DESCRIPTION = models.TextField(max_length=500)
	MARCA=models.TextField(max_length=200)
	LONG_DESCRIPTION=models.TextField(max_length=500)
	ITEM_TYPE=models.TextField(max_length=10)
	PRIMARY_UOM_CODE=models.CharField(max_length=100)
	SECONDARY_UOM_CODE=models.CharField(max_length=5,blank=True, null=True)
	SECONDARY_DEFAULT_IND=models.CharField(max_length=5,blank=True, null=True)
	ATTRIBUTE_CATEGORY=models.CharField(max_length=10,blank=True, null=True)
	ATTRIBUTE1=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE2=models.CharField(max_length=200,blank=True, null=True)
	GRUPO=models.CharField(max_length=10,blank=True, null=True)
	ATTRIBUTE3=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE4=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE5=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE6=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE7=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE8=models.CharField(max_length=200,blank=True, null=True)
	#ESPACIO EN BLANCO
	ATTRIBUTE9=models.CharField(max_length=500,blank=True, null=True)
	SUBGRUPO=models.CharField(max_length=100,blank=True, null=True)
	ARTICULO=models.CharField(max_length=100,blank=True, null=True)
	ATTRIBUTE11=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE12=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE13=models.CharField(max_length=200,blank=True, null=True)
	#ESPACIO EN BLANCO
	ATTRIBUTE14=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE15=models.CharField(max_length=200,blank=True, null=True)
	GLOBAL_ATTRIBUTE8=models.CharField(max_length=200,blank=True, null=True)
	GLOBAL_ATTRIBUTE1=models.CharField(max_length=200,blank=True, null=True)
	GLOBAL_ATTRIBUTE2=models.CharField(max_length=200,blank=True, null=True)
	GLOBAL_ATTRIBUTE3=models.CharField(max_length=200,blank=True, null=True)
	GLOBAL_ATTRIBUTE4=models.CharField(max_length=200,blank=True, null=True)
	GLOBAL_ATTRIBUTE5=models.CharField(max_length=200,blank=True, null=True)
	SHELF_LIFE_DAYS=models.CharField(max_length=200,blank=True, null=True)
	TEST_INTERVAL=models.CharField(max_length=200,blank=True, null=True)
	EXPIRATION_ACTION_INTERVAL=models.CharField(max_length=200,blank=True, null=True)
	EXPIRATION_ACTION_CODE=models.CharField(max_length=200,blank=True, null=True)
	MATURITY_DAYS=models.CharField(max_length=200,blank=True, null=True)
	HOLD_DAYS=models.CharField(max_length=200,blank=True, null=True)
	SERIAL_NUMBER_CONTROL_CODE=models.CharField(max_length=200,blank=True, null=True)
	AUTO_SERIAL_ALPHA_PREFIX=models.CharField(max_length=200,blank=True, null=True)
	START_AUTO_SERIAL_NUMBER=models.CharField(max_length=200,blank=True, null=True)
	LOCATION_CONTROL_CODE=models.CharField(max_length=200,blank=True, null=True)
	RESTRICT_SUBINVENTORIES_CODE=models.CharField(max_length=200,blank=True, null=True)
	RESTRICT_LOCATORS_CODE=models.CharField(max_length=200,blank=True, null=True)
	LOT_STATUS_ENABLED=models.CharField(max_length=200,blank=True, null=True)
	DEFAULT_LOT_STATUS_ID=models.CharField(max_length=200,blank=True, null=True)
	COSTOVENTAS=models.CharField(max_length=200,blank=True, null=True)
	BUYER_ID=models.CharField(max_length=200,blank=True, null=True)
	LIST_PRICE_PER_UNIT=models.CharField(max_length=200,blank=True, null=True)
	GASTOS=models.CharField(max_length=200,blank=True, null=True)
	COMPROMISO=models.CharField(max_length=200,blank=True, null=True)
	WEIGHT_UOM_CODE=models.CharField(max_length=200,blank=True, null=True)
	CODIGO=models.CharField(max_length=200,blank=True, null=True)
	VOLUME_UOM_CODE=models.CharField(max_length=200,blank=True, null=True)
	UNIT_VOLUME=models.CharField(max_length=200,blank=True, null=True)
	UNIT_LENGTH=models.CharField(max_length=200,blank=True, null=True)
	UNIT_WIDTH=models.CharField(max_length=200,blank=True, null=True)
	UNIT_HEIGHT=models.CharField(max_length=200,blank=True, null=True)
	INVENTORY_PLANNING_CODE=models.CharField(max_length=200,blank=True, null=True)
	PLANNER_CODE=models.CharField(max_length=200,blank=True, null=True)
	PLANNING_MAKE_BUY_CODE=models.CharField(max_length=200,blank=True, null=True)
	MIN_MINMAX_QUANTITY=models.CharField(max_length=200,blank=True, null=True)
	MAX_MINMAX_QUANTITY=models.CharField(max_length=200,blank=True, null=True)
	MINIMUM_ORDER_QUANTITY=models.CharField(max_length=200,blank=True, null=True)
	MAXIMUM_ORDER_QUANTITY=models.CharField(max_length=200,blank=True, null=True)
	FIXED_ORDER_QUANTITY=models.CharField(max_length=200,blank=True, null=True)
	FIXED_DAYS_SUPPLY=models.CharField(max_length=200,blank=True, null=True)
	FIXED_LOT_MULTIPLIER=models.CharField(max_length=200,blank=True, null=True)
	SOURCE_TYPE=models.CharField(max_length=200,blank=True, null=True)
	MRP_PLANNING_CODE=models.CharField(max_length=200,blank=True, null=True)
	TAX_CODE=models.CharField(max_length=200,blank=True, null=True)
	VENTAS=models.CharField(max_length=200,blank=True, null=True)
	PROCESS_YIELD_SUBINVENTORY=models.CharField(max_length=200,blank=True, null=True)
	SEGMENT1_1=models.CharField(max_length=200,blank=True, null=True)
	SEGMENT2=models.CharField(max_length=200,blank=True, null=True)
	SEGMENT3=models.CharField(max_length=200,blank=True, null=True)
	SEGMENT4=models.CharField(max_length=200,blank=True, null=True)
	SEGMENT5=models.CharField(max_length=200,blank=True, null=True)
	SO_TRANSACTIONS_FLAG=models.CharField(max_length=200,blank=True, null=True)
	TAXABLE_FLAG=models.CharField(max_length=200,blank=True, null=True)
	PURCHASING_TAX_CODE=models.CharField(max_length=200,blank=True, null=True)




	def __unicode__(self):
		return str(self.SEGMENT1)
