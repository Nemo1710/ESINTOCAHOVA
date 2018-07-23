#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist


from django.shortcuts import render
from tablib import Dataset
import csv
import sys
from tomafisica.models import Bodegas

#from .models import ProductoBodega
from busqueda.models import Productos
from busqueda.models import PEC

from .models import ConfUsuario

#
# Create your views here.
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def pec(request):
	auxiliar = 1
	if auxiliar == 1:

		csv.register_dialect('pipes', delimiter=str(u'|'))

		with open('/home/PECTOTAL.csv', 'r') as f:
			reader = csv.reader(f, dialect='pipes')

			i = 0
			for row in reader:

				if i >= 1:
					# ejemplos=(row[4])
					# print (ejemplos)
					# if ejemplos is None:
					#	ejemplos='-1'
					# ejemplo= '"'+ejemplos+'"'

					# ejemplo=row[4]
					# ejemplo=ejemplo.decode('utf-8')


					obj = PEC.objects.create(
						SEGMENT1=row[1],


					)
				i = i + 1


			# print(row[0]+"|"+row[1]+"|"+row[2]+"|"+row[3]+"|"+row[4]+"|"+row[5]+"|"+row[6]+"|"+row[7]+"|"+row[8]+"|"+row[9]
			#       +"|"+row[10]+"|"+row[11]+"|"+row[12]+"|"+row[13]+"|"+row[14]+"|"+row[15]+"|"+row[16]+"|"+row[17]
			#      +"|"+row[18]+"|"+row[19]+"|"+row[20]+"|"+row[21]+"|"+row[22]+"|"+row[23]+"|"+row[24]+"|"+row[25])

	return render(request, 'formulario.html')


#para subir data total
def formu(request):
	auxiliar=1
	if auxiliar==1:


		csv.register_dialect('pipes', delimiter=str(u'|'))


		with open('/home/finafinalfinal.csv', 'r') as f:
		    reader = csv.reader(f, dialect='pipes')

		    i=0
		    for row in reader:

		        if i>=1:

		            #ejemplos=(row[4])
		            #print (ejemplos)
		            #if ejemplos is None:
		            #	ejemplos='-1'
		            #ejemplo= '"'+ejemplos+'"'

		            #ejemplo=row[4]
		            #ejemplo=ejemplo.decode('utf-8')


					obj = Productos.objects.create(
		            	ORGANIZATION_CODE=row[0],
		            	SEGMENT1 = row[1],
						CATALOGACION=row[2],
						CLASE=row[3],
						DESCRIPTION =row[4].decode('latin-1'),
						MARCA= "",
						LONG_DESCRIPTION=row[5].decode('latin-1'),
						ITEM_TYPE=row[6],
						PRIMARY_UOM_CODE=row[7].decode('latin-1'),
						SECONDARY_UOM_CODE=row[8],
						SECONDARY_DEFAULT_IND=row[9],
						ATTRIBUTE_CATEGORY=row[10].decode('latin-1'),
						ATTRIBUTE1=row[11].decode('latin-1'),
						ATTRIBUTE2=row[12].decode('latin-1'),
						GRUPO=row[13],
						ATTRIBUTE3=row[14].decode('latin-1'),
						ATTRIBUTE4=row[15].decode('latin-1'),
						ATTRIBUTE5=row[16].decode('latin-1'),
						ATTRIBUTE6=row[17].decode('latin-1'),
						ATTRIBUTE7=row[18].decode('latin-1'),
						ATTRIBUTE8=row[19].decode('latin-1'),
						#ESPACIO EN BLANCO
						ATTRIBUTE9=row[21].decode('latin-1'),
						SUBGRUPO=row[22].decode('latin-1'),
						ARTICULO=row[23].decode('latin-1'),
						ATTRIBUTE11=row[24].decode('latin-1'),
						ATTRIBUTE12=row[25].decode('latin-1'),
						ATTRIBUTE13=row[26].decode('latin-1'),
						#ESPACIO EN BLANCO
						ATTRIBUTE14=row[28].decode('latin-1'),
						ATTRIBUTE15=row[29].decode('latin-1'),
						GLOBAL_ATTRIBUTE8=row[30].decode('latin-1'),
						GLOBAL_ATTRIBUTE1=row[31].decode('latin-1'),
						GLOBAL_ATTRIBUTE2=row[32].decode('latin-1'),
						GLOBAL_ATTRIBUTE3=row[33].decode('latin-1'),
						GLOBAL_ATTRIBUTE4=row[34].decode('latin-1'),
						GLOBAL_ATTRIBUTE5=row[35].decode('latin-1'),
						SHELF_LIFE_DAYS=row[36].decode('latin-1'),
						TEST_INTERVAL=row[37],
						EXPIRATION_ACTION_INTERVAL=row[38].decode('latin-1'),
						EXPIRATION_ACTION_CODE=row[39].decode('latin-1'),
						MATURITY_DAYS=row[40],
						HOLD_DAYS=row[41],
						SERIAL_NUMBER_CONTROL_CODE=row[42],
						AUTO_SERIAL_ALPHA_PREFIX=row[43],
						START_AUTO_SERIAL_NUMBER=row[44],
						LOCATION_CONTROL_CODE=row[45],
						RESTRICT_SUBINVENTORIES_CODE=row[46],
						RESTRICT_LOCATORS_CODE=row[47],
						LOT_STATUS_ENABLED=row[48],
						DEFAULT_LOT_STATUS_ID=row[49],
						COSTOVENTAS=row[50],
						BUYER_ID=row[51],
						LIST_PRICE_PER_UNIT=row[52],
						GASTOS=row[53],
						COMPROMISO=row[54],
						WEIGHT_UOM_CODE=row[55],
						CODIGO=row[56],
						VOLUME_UOM_CODE=row[57],
						UNIT_VOLUME=row[58],
						UNIT_LENGTH=row[59],
						UNIT_WIDTH=row[60],
						UNIT_HEIGHT=row[61],
						INVENTORY_PLANNING_CODE=row[62],
						PLANNER_CODE=row[63],
						PLANNING_MAKE_BUY_CODE=row[64],
						MIN_MINMAX_QUANTITY=row[65],
						MAX_MINMAX_QUANTITY=row[66],
						MINIMUM_ORDER_QUANTITY=row[67],
						MAXIMUM_ORDER_QUANTITY=row[68],
						FIXED_ORDER_QUANTITY=row[69],
						FIXED_DAYS_SUPPLY=row[70],
						FIXED_LOT_MULTIPLIER=row[71],
						SOURCE_TYPE=row[72],
						MRP_PLANNING_CODE=row[73],
						TAX_CODE=row[74],
						VENTAS=row[75],
						PROCESS_YIELD_SUBINVENTORY=row[76],
						SEGMENT1_1=row[77],
						SEGMENT2=row[78],
						SEGMENT3=row[79],
						SEGMENT4=row[80],
						SEGMENT5=row[81],
						SO_TRANSACTIONS_FLAG=row[82],
						TAXABLE_FLAG=row[83],
						PURCHASING_TAX_CODE=row[84],



		            )
		        i=i+1


		            # print(row[0]+"|"+row[1]+"|"+row[2]+"|"+row[3]+"|"+row[4]+"|"+row[5]+"|"+row[6]+"|"+row[7]+"|"+row[8]+"|"+row[9]
		            #       +"|"+row[10]+"|"+row[11]+"|"+row[12]+"|"+row[13]+"|"+row[14]+"|"+row[15]+"|"+row[16]+"|"+row[17]
		            #      +"|"+row[18]+"|"+row[19]+"|"+row[20]+"|"+row[21]+"|"+row[22]+"|"+row[23]+"|"+row[24]+"|"+row[25])


	return render(request, 'formulario.html')

#subir corte de bodega
def bodega(request):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')
	csv.register_dialect('pipes', delimiter=str(u'|'))
	with open(r'/home/bodega3.csv'.decode('utf8'), 'r') as f:

		reader = csv.reader(f, dialect='pipes')
		i=0
		for row in reader:
			if i>=1:

				obj = Bodegas.objects.create(
		            	ORGANIZATION_CODE ="B07",
						SEGMENT1 = row[0],
						ANTERIOR = row[1].decode('latin-1'),
						DESCRIPTION = row[2].decode('latin-1'),
						ATTRIBUTE3=row[3].decode('latin-1'),#fabricante
						ATTRIBUTE4=row[4].decode('latin-1'),#numero de parte o serie
						CANTIDAD=row[5],
						PRIMARY_UOM_CODE=row[6],#unidad de medida
						LOCALIZADOR=row[7],

		            )
			i=i+1



	return render(request, 'formulario.html')

from catalogacion.models import DFinales
def subirdigitos(request):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')
	csv.register_dialect('pipes', delimiter=str(u'|'))
	with open(r'/home/DFinalesC08.csv', 'r') as f:
		reader = csv.reader(f, dialect='pipes')
		for row in reader:
			obj = DFinales.objects.create(
				Entero=row[0],
				Fraccion=row[1].decode('latin-1'),
				Digitos=row[2],
				Clases=row[3]
			)
	return render(request, 'formulario.html')

from catalogacion.models import SGrupo
def subirsubgrupos(request):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')
	csv.register_dialect('pipes', delimiter=str(u'|'))
	with open(r'/home/Subgrupos.csv', 'r') as f:
		reader = csv.reader(f, dialect='pipes')
		for row in reader:
			obj = SGrupo.objects.create(
				Subgrupo=row[0],
				Titulo=row[1].decode('latin-1'),
				Cod=row[2]
			)
	return render(request, 'formulario.html')

##
from catalogacion.models import Grupos

def subirgrupos(request):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')
	csv.register_dialect('pipes', delimiter=str(u'|'))
	with open(r'/home/gruposC7.csv', 'r') as f:
		reader = csv.reader(f, dialect='pipes')
		for row in reader:
			obj = Grupos.objects.create(
				Grupo=row[0],
				Titulo= row[1].decode('latin-1'),
				Clase_id="2"
			)
	return render(request, 'formulario.html')



def inicio(request):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/login')
	return render(request, 'principal.html')







def error(request):

	return render(request, 'error.html')


def bodegatrabajo(request):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')

	res=ConfUsuario.objects.get(user=request.user)

	dict = {

		'valores': res,


	}
	return render(request, 'bodega.html', dict)


def error3(request):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/login')
	return render(request, 'error3.html')












