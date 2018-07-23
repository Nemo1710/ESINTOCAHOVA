#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

class HCodigoForm(forms.Form):
    Nombre = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el codigo'}))


class HomologacionForm(forms.Form):
    #Celular = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un numero celular de contacto que cuente con Whatsapp de preferencia'}))
    Descripcion = forms.CharField(widget=forms.Textarea(attrs={'cols': 25, 'rows': 4, 'class': 'form-control', 'placeholder': 'Ingresa la descripción'}),required=False)
    Description = forms.CharField(widget=forms.Textarea(attrs={'cols': 25, 'rows': 4, 'class': 'form-control', 'placeholder': 'Enter the description'}),required=False)
    Descripcion_Larga = forms.CharField(widget=forms.Textarea(attrs={'cols': 25, 'rows': 4, 'class': 'form-control', 'placeholder': 'Ingresa la descripción larga'}),required=False)
    Description_Long = forms.CharField(widget=forms.Textarea(attrs={'cols': 25, 'rows': 4, 'class': 'form-control', 'placeholder': 'Enter Long Description'}),required=False)

