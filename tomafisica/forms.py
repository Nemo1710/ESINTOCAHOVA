#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from tomafisica.models import Unidades



class CodigoForm(forms.Form):
    Nombre = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el codigo'}))


IMP_CHOICES = (
    ('amp', 'amp'),
    ('bag', 'bag'),
    ('bag', 'bag'),
    ('bot', 'bot'),
    ('bag', 'bag'),
    ('box', 'box'),
    ('can', 'can'),
    ('cm', 'cm'),
    ('cyl', 'cyl'),
    ('dr', 'dr'),
    ('ea', 'ea'),
    ('ft', 'ft'),
    ('ft2', 'ft3'),
    ('g', 'g'),
    ('gal', 'gal'),
    ('glb', 'glb'),
    ('in', 'in'),
    ('jgo', 'jgo'),
    ('jt', 'jt'),
    ('kg', 'kg'),
    ('kit', 'kit'),
    ('L', 'L'),
    ('lb', 'lb'),
    ('m', 'm'),
    ('m2', 'm3'),
    ('ml', 'ml'),
    ('MWh', 'MWh'),
    ('pck', 'pck'),
    ('pr', 'pr'),
    ('ro', 'ro'),
    ('sak', 'sak'),
    ('set', 'set'),
    ('sht', 'sht'),
    ('t', 't'),



)

class CantidadForm(forms.Form):
    cantidad = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa cantidad actual'}))


class TfisicaForm(forms.Form):
    #Celular = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un numero celular de contacto que cuente con Whatsapp de preferencia'}))
    Cantidad= forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': u'Ingresa cantidad contada'}))
    Unidad_de_Medida=forms.ChoiceField(choices=IMP_CHOICES, required=True,widget=forms.Select(attrs={'class': 'form-control'}))