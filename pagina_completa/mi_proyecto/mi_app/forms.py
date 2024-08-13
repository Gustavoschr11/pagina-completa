from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'mensaje', 'pregunta1', 'pregunta2', 'pregunta3', 'pregunta4', 'pregunta5']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
            'pregunta1': forms.TextInput(attrs={'class': 'form-control'}),
            'pregunta2': forms.TextInput(attrs={'class': 'form-control'}),
            'pregunta3': forms.TextInput(attrs={'class': 'form-control'}),
            'pregunta4': forms.TextInput(attrs={'class': 'form-control'}),
            'pregunta5': forms.TextInput(attrs={'class': 'form-control'}),
        }
