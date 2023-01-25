from django import forms
from django.forms import ModelForm 
from django.forms import widgets 
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Pastel, Cliente

class PastelForm(forms.ModelForm):
    
    class Meta: 
        model = Pastel
        fields = ['codigo', 'relleno', 'categoria', 'imagen']
        labels = {
            'codigo': 'Codigo',
            'relleno': 'Relleno',
            'categoria': 'Categoria',
            'imagen': 'Imagen'
        }
        widgets={
            'codigo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite un codigo',
                    'id': 'codigo'
                }
            ),
            'relleno': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Digite su relleno',
                    'id': 'relleno'
                }
            ),
            'categoria':forms.Select(
                attrs = {
                    'class': 'form-control',
                    'id': 'categoria'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen',
                }
            )
        }


class ClienteForm(forms.ModelForm):
    
    class Meta: 
        model = Cliente 
        fields = ['rut', 'nombre', 'edad']
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'edad': 'Edad',
        }
        widgets={
            'rut': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite rut del cliente',
                    'id1': 'rut'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Digite nombre completo del cliente',
                    'id1': 'nombre'
                }
            ),
            'edad': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Digite edad del cliente',
                    'id1': 'edad'
                }
            ),
            'categoria':forms.Select(
                attrs = {
                    'class': 'form-control',
                    'id1': 'categoria'
                }
            ),
        }