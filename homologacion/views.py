# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from busqueda.models import PEC
from homologacion.forms import HomologacionForm
from busqueda.models import Productos
from .forms import HCodigoForm


def homologacion(request):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')

	form = HCodigoForm(request.POST or None)
	#print "hola hola"
	if form.is_valid():
		#print "ya llego"
		form_data = form.cleaned_data
		codigo = form_data.get("Nombre")
		return redirect('http://159.89.189.145/homologacion/' + str(codigo))
		#print codigo
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
		return render(request, 'homologacion.html', dict)

	dict = {

		'form': form,
		'boton': True,
	}

	return render(request, 'homologacion.html', dict)


def homologacion1(request,codigo):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')

	form =HomologacionForm(request.POST or None)

	try:
		objPROD = Productos.objects.filter(SEGMENT1=codigo)[:1]
	except:
		return redirect('http://159.89.189.145/noexiste')



	if form.is_valid():
		#print "ya llego"
		form_data = form.cleaned_data
		descripcion = form_data.get("Descripcion")
		description = form_data.get("Description")
		descripcion_larga = form_data.get("Descripcion_Larga")
		descripcion_long = form_data.get("Descripcion_Larga")
		if descripcion:
			consulta = PEC.objects.get(SEGMENT1=codigo)
			consulta.MARCA = str(grupo.Grupo)
			consulta.save()


	dict = {
		'caracteristica': objPROD,
		'claseform':  form,
		'mensaje': "El producto que buscas ya ha sido contado para la toma física",
		'val': False,

	}
	return render(request, 'catalogacion1.html', dict)
