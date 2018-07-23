# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from busqueda.models import PEC
from busqueda.models import Bodega


class Bodegas(models.Model):
	ORGANIZATION_CODE = models.CharField(max_length=5)
	SEGMENT1 = models.CharField(max_length=15)
	ANTERIOR = models.CharField(max_length=200)
	DESCRIPTION = models.TextField(max_length=200)
	ATTRIBUTE3=models.CharField(max_length=200,blank=True, null=True)
	ATTRIBUTE4=models.CharField(max_length=200,blank=True, null=True)
	CANTIDAD=models.CharField(max_length=10,blank=True, null=True)
	PRIMARY_UOM_CODE=models.CharField(max_length=10)
	LOCALIZADOR=models.CharField(max_length=8)


class Unidades(models.Model):
	Titulo= models.CharField(max_length=10)

	def __unicode__(self):
		return str(self.Titulo)


class ProductoBodega(models.Model):
	Producto=models.ForeignKey(PEC,on_delete=models.CASCADE)
	Bodega=models.ForeignKey(Bodega,on_delete=models.CASCADE)
	Cantidad=models.CharField(max_length=20)

	def __unicode__(self):
		return str(self.Producto)