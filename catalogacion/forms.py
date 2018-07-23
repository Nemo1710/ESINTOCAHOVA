#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from .models import Clases
from .models import Grupos
from .models import SGrupo
from .models import DFinales

#fsfdsf
class CCodigoForm(forms.Form):
    Nombre = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el codigo'}))


class ClaseForm(forms.Form):
    Clase=forms.ModelChoiceField(queryset=Clases.objects.all().order_by('Clase'), required=True,widget=forms.Select(attrs={'class': 'form-control'}))

class GrupoForm(forms.Form):
    Grupo = forms.ModelChoiceField(queryset=Grupos.objects.all(),required=True,widget=forms.Select(attrs={'class': 'form-control'}))
    #Grupo = forms.ModelChoiceField(queryset=Grupos.objects.filter(Clase_id=site_id).order_by('Grupo'), required=True,widget=forms.Select(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        self.dato = kwargs.pop('dato')
        super(GrupoForm, self).__init__(*args, **kwargs)
        self.fields['Grupo'].queryset = Grupos.objects.filter(Clase_id= str(self.dato))

class SubGrupoForm(forms.Form):
    Subgrupo = forms.ModelChoiceField(queryset=SGrupo.objects.all(),required=True,widget=forms.Select(attrs={'class': 'form-control'}))
    #Grupo = forms.ModelChoiceField(queryset=Grupos.objects.filter(Clase_id=site_id).order_by('Grupo'), required=True,widget=forms.Select(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        self.dato = kwargs.pop('dato')
        super(SubGrupoForm, self).__init__(*args, **kwargs)
        self.fields['Subgrupo'].queryset = SGrupo.objects.filter(Cod= str(self.dato))

class DigitosFinalesForm(forms.Form):
    DigitosFinales = forms.ModelChoiceField(queryset=DFinales.objects.all(),required=True,widget=forms.Select(attrs={'class': 'form-control'}))
    ##Grupo = forms.ModelChoiceField(queryset=Grupos.objects.filter(Clase_id=site_id).order_by('Grupo'), required=True,widget=forms.Select(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        self.dato = kwargs.pop('dato')
        super(DigitosFinalesForm, self).__init__(*args, **kwargs)
        self.fields['DigitosFinales'].queryset = DFinales.objects.filter(Clases= str(self.dato))

