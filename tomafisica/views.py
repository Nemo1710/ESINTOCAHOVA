# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import CodigoForm
from busqueda.models import Productos
from busqueda.models import PEC
from tomafisica.models import Bodegas
from tomafisica.models import ProductoBodega
from busqueda.models import Bodega
from busqueda.models import ConfUsuario
from busqueda.models import PEC
from .forms import TfisicaForm
from .forms import CantidadForm



from django.shortcuts import render
import csv



def tomafisica(request):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')

	form =CodigoForm(request.POST or None)
	print "hola hola"
	if form.is_valid():
		#print "ya llego"
		form_data = form.cleaned_data
		codigo = form_data.get("Nombre")
		return redirect('http://159.89.189.145/tomafisica/'+str(codigo))
		#print codigo
		#valores=Productos.objects.filter(SEGMENT1=codigo)
		valores1 = Bodegas.objects.filter(SEGMENT1=codigo)
		valores2 = Productos.objects.filter(SEGMENT1=codigo).order_by('ORGANIZATION_CODE')

		form =CodigoForm(request.POST or None)


		dict = {

				'valores': valores1,
				'valores2': valores2,
				'boton':False,

				'dato':"1",

				}
		return render(request, 'tomafisica.html',dict)

	dict = {


				'form': form,
				'boton': True,
			}


	return render(request, 'tomafisica.html',dict)



def tomafisica1(request,codigo):
	if not request.user.is_authenticated():
		return redirect('http://159.89.189.145/error')

	form =TfisicaForm(request.POST or None)
	res = ConfUsuario.objects.get(user=request.user)
	bodega1 = res.bodega.Nombre
	try:
		objPROD = Productos.objects.get(SEGMENT1=codigo, ORGANIZATION_CODE=bodega1)
	except ObjectDoesNotExist:
		return redirect('http://159.89.189.145/error3')

	objPEC = PEC.objects.get(SEGMENT1=codigo)
	objBod = Bodega.objects.get(Nombre=bodega1)



	if form.is_valid():

		form_data = form.cleaned_data
		cantidad = form_data.get("Cantidad")
		unidad = form_data.get("Unidad_de_Medida")

		ProductoBodega.objects.create(Producto=objPEC,Bodega=objBod,Cantidad=cantidad)


		if 'lcantidad' in request.POST:

			valores1 = Bodegas.objects.get(SEGMENT1=codigo, ORGANIZATION_CODE=res.bodega.Nombre)

		redirect('http://159.89.189.145/siguiente')




	bodega=res.bodega.Nombre
	nombre=res.bodega.Localizacion
	try:
		resres=ProductoBodega.objects.get(Producto=objPEC,Bodega=objBod)
	except ObjectDoesNotExist:
		#redirect('http://159.89.189.145/error2')
		valores1 = Bodegas.objects.filter(SEGMENT1=codigo, ORGANIZATION_CODE=res.bodega.Nombre)

		valores2 = Productos.objects.filter(SEGMENT1=codigo, ORGANIZATION_CODE=res.bodega.Nombre).order_by(
			'ORGANIZATION_CODE')

		# form = CodigoForm(request.POST or None)

		dict = {

			'valores': valores1,
			'valores2': valores2,
			'boton': False,
			'bodega': bodega,
			'nombre': nombre,
			'form': form,
			'dato': "1",
			'codigo': codigo,
			'val': True,

		}
		return render(request, 'tomafisica1.html', dict)
	dict = {

		'codigo': codigo,
		'mensaje': "El producto que buscas ya ha sido contado para la toma física",
		'val': False,

	}
	return render(request, 'tomafisica1.html', dict)
