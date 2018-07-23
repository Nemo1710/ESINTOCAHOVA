# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Clases(models.Model):
	Clase = models.CharField(max_length=2)
	Titulo = models.CharField(max_length= 100)
	Descripcion = models.TextField(blank=True, null=True)
	def __unicode__(self):
		return "Clase: "+str(self.Clase)+" "+str(self.Titulo)



class Grupos(models.Model):
    Clase = models.ForeignKey(Clases)
    Grupo = models.CharField(max_length=2)
    Titulo = models.CharField(max_length=100)
    def __unicode__(self):
        return "Grupo: " + str(self.Grupo) +",  "+str(self.Titulo)#+', '+ str(self.Clase)


class SGrupo(models.Model):
	Clases = models.ForeignKey(Clases,null=True)
	Grupos = models.ForeignKey(Grupos,null=True)
	Cod = models.CharField(max_length= 4,null=True)
	Subgrupo = models.CharField(max_length= 2)
	Titulo = models.CharField(max_length= 100)
	def __unicode__(self):
		return "Subgrupo: "+str(self.Subgrupo)+',  '+str(self.Titulo)

class DFinales(models.Model):
	##Clases = models.ForeignKey(Clases, null=True)
	Clases = models.CharField(max_length=2)
	##Cod = models.CharField(max_length=4, null=True)
	Digitos = models.CharField(max_length=3)
	Fraccion = models.CharField(max_length=10)
	Entero = models.CharField(max_length=10)

	def __unicode__(self):
		return "Medida: " + str(self.Entero) + '  ' + str(self.Fraccion)
