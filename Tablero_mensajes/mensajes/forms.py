# mensajes/forms.py
from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['texto', 'remitente', 'destinatario']
        widgets = {
            'texto': forms.Textarea(attrs={'class': 'form-control'}),
            'remitente': forms.TextInput(attrs={'class': 'form-control'}),
            'destinatario': forms.TextInput(attrs={'class': 'form-control'}),
        }

class FiltroMensajeForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False, label='Filtrar por nombre')
