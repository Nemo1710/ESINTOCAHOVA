# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CCodigoForm
from busqueda.models import PEC
from busqueda.models import Productos
from .forms import ClaseForm
from .forms import GrupoForm
from .forms import SubGrupoForm
from .forms import DigitosFinalesForm
from .models import Clases
from .models import Grupos
from .models import SGrupo
from django.core.exceptions import ObjectDoesNotExist
from .models import DFinales




def clases(request):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/login')

	Datos = Clases.objects.all()
	dict = {

		'valores': Datos,
	}

	return render(request, 'clases.html',dict)


def catalogacion(request):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')

	form = CCodigoForm(request.POST or None)
	mensaje = ''
	#print "hola hola"
	if form.is_valid():
		#print "ya llego"
		form_data = form.cleaned_data
		codigo = form_data.get("Nombre")
		try:
			existe = PEC.objects.get(SEGMENT1=codigo )
			cod = existe.CODIGO
			if cod is not None:
				#mensaje = 'El articulo ya fue codigicado como: ' + cod
				return redirect('http://159.89.189.145/catalogado/'+ str(codigo))
		except:
			mensaje = ' '

		return redirect('http://159.89.189.145/catalogacion/' + str(codigo))

		# valores=Productos.objects.filter(SEGMENT1=codigo)
		valores1 = Bodegas.objects.filter(SEGMENT1=codigo)
		valores2 = Productos.objects.filter(SEGMENT1=codigo).order_by('ORGANIZATION_CODE')

		form = CodigoForm(request.POST or None)

		dict = {

			'valores': valores1,
			'valores2': valores2,
			'boton': False,
			'dato': "1",

		}
		return render(request, 'catalogacion.html', dict)

	dict = {
		'mensaje' : mensaje,
		'form': form,
		'boton': True,
	}

	return render(request, 'catalogacion.html', dict)


def catalogado (request,codigo):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')
	objPROD = Productos.objects.filter(SEGMENT1=codigo)[:1]
	existe = PEC.objects.get(SEGMENT1=codigo)
	cod = existe.CODIGO
	mensaje ='El Articulo ya fue Codificado como: '+cod
	if 'latras' in request.POST:
		return redirect('http://159.89.189.145/catalogacion')

	elif 'lcodificar' in request.POST:
		return redirect('http://159.89.189.145/catalogacion/'+ str(codigo))

	dict = {
		'caracteristica': objPROD,
		'mensaje': mensaje,
		'val': False,

	}
	return render(request, 'catalogado.html', dict)

def catalogacion1(request,codigo):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')

	form =ClaseForm(request.POST or None)
	#objPROD = Productos.objects.filter(SEGMENT1=codigo)[:1]
	try:
		objPROD = Productos.objects.filter(SEGMENT1=codigo)[:1]# ORGANIZATION_CODE=bodega1)
	except ObjectDoesNotExist:
		return redirect('http://159.89.189.145/error3')

	if form.is_valid():
			form_data = form.cleaned_data
			clase = form_data.get("Clase")
			#print codigo

			consulta=PEC.objects.get(SEGMENT1=codigo)
			consulta.CLASE=str(clase.Clase)
			consulta.save()
			return redirect('http://159.89.189.145/catalogacion/grupo/' + str(codigo))




	dict = {
		'caracteristica': objPROD,
		'claseform':  form,
		#'grupoform': form1,
		'mensaje': '',
		'val': False,

	}
	return render(request, 'catalogacion1.html', dict)



def catalogacion2(request,codigo):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')
#
	consulta = PEC.objects.get(SEGMENT1=codigo)
	objPROD = Productos.objects.filter(SEGMENT1=codigo)[:1]
	datoclase = consulta.CLASE
	consultagrup = Clases.objects.get(Clase = datoclase)
	dato = consultagrup.id
	# print dato
	form1 = GrupoForm(request.POST or None, dato=dato)


	if form1.is_valid():
		form1_data = form1.cleaned_data
		grupo = form1_data.get("Grupo")
		# print codigo

		consulta = PEC.objects.get(SEGMENT1=codigo)
		consulta.GRUPO = str(grupo.Grupo)
		consulta.save()

		return redirect('http://159.89.189.145/catalogacion/subgrupo/' + str(codigo))

	dict = {
		'caracteristica': objPROD,
		#'claseform': form,
		'grupoform': form1,
		'dato': datoclase,
		'mensaje': " ",
		'val': False,

	}
	return render(request, 'catalogacion2.html', dict)



def catalogacion3(request,codigo):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')
#
	consulta = PEC.objects.get(SEGMENT1=codigo)
	objPROD = Productos.objects.filter(SEGMENT1=codigo)[:1]
	dato1 = str(consulta.CLASE)
	dato2 = str(consulta.GRUPO)

	if dato1 == '08' or dato1=='05' or dato1=='07':
		dato ='00'+dato1

	else:
		dato = dato1+dato2

	#dato = dato1+dato2
	#if dato1 == '05':
	form1 = SubGrupoForm(request.POST or None, dato=dato)


	if form1.is_valid():
		form1_data = form1.cleaned_data
		grupo = form1_data.get("Subgrupo")
		## print codigo

		consulta = PEC.objects.get(SEGMENT1=codigo)
		consulta.SUBGRUPO = str(grupo.Subgrupo)
		consulta.save()

		return redirect('http://159.89.189.145/catalogacion/3digitos/' + str(codigo))

	dict = {
		'caracteristica': objPROD,
		#'claseform': form,
		'grupoform': form1,
		'dato': dato1,
		'dato2': dato2,
		'mensaje': " ",
		'val': False,

	}
	return render(request, 'catalogacion3.html', dict)




def catalogacion4(request,codigo):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')
#
	consulta = PEC.objects.get(SEGMENT1=codigo)
	objPROD = Productos.objects.filter(SEGMENT1=codigo)[:1]
	dato1 = str(consulta.CLASE)
	dato2 = str(consulta.GRUPO)
	dato3 = str(consulta.SUBGRUPO)

	if dato1 == '08':
		form1 = DigitosFinalesForm(request.POST or None, dato=dato1)


	if form1.is_valid():
		form1_data = form1.cleaned_data
		grupo = form1_data.get("DigitosFinales")
		#print codigo

		consulta = PEC.objects.get(SEGMENT1=codigo)
		consulta.DIGITOSFINALES = str(grupo.Digitos)
		consulta.save()
		return redirect('http://159.89.189.145/catalogacion/confirmacion/' + str(codigo))

	dict = {
		'caracteristica': objPROD,
		#'claseform': form,
		'grupoform': form1,
		'dato': dato1,
		'dato2': dato2,
		'dato3' : dato3,
		'mensaje': "",
		'val': False,

	}
	return render(request, 'catalogacion4.html', dict)



def catalogacion5(request,codigo):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')
#
	consulta = PEC.objects.get(SEGMENT1=codigo)
	objPROD = Productos.objects.filter(SEGMENT1=codigo)[:1]
	dato1 = str(consulta.CLASE)
	dato2 = str(consulta.GRUPO)
	dato3 = str(consulta.SUBGRUPO)
	dato4 = str(consulta.DIGITOSFINALES)
	dato = dato1+dato2+dato3+dato4

	try:
		duplicidad = PEC.objects.get(CODIGO=dato)

		if str(duplicidad.SEGMENT1) == str(codigo):
			if str(duplicidad.CODIGO) == str(dato):
				mensaje = 'Articulo anteriormente codificado con el mismo codigo'
			elif str(duplicidad.CODIGO) != str(dato):
				mensaje = 'Articulo anteriormente codificado con el codigo'+str(duplicidad.CODIGO)
		else:
			mensaje = 'CODIGO DUPLICADO!!!'
	except:
		mensaje = 'CODIGO DISPONIBLE'

	if 'lconfirmar' in request.POST:
		consulta = PEC.objects.get(SEGMENT1=codigo)
		consulta.CODIGO = str(dato)
		consulta.save()
		return redirect('http://159.89.189.145/catalogacion')

	elif 'lrevision' in request.POST:
		print 'revision'

	dict = {
		'caracteristica': objPROD,
		#'claseform': form,
		#'grupoform': form1,
		'dato': dato1,
		'dato2': dato2,
		'dato3' : dato3,
		'dato4' : dato4,
		'mensaje': mensaje,
		'val': False,
	}
	return render(request, 'catalogacion5.html', dict)
