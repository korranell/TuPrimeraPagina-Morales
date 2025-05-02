from django import forms
from .models import Transaccion

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['descripcion', 'categoria', 'monto', 'fecha', 'imagen',]
        widgets = {
            'descripcion': forms.TextInput(attrs={'placeholder': 'Descripción', 'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'placeholder': 'Categoria', 'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'placeholder': 'Monto', 'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'descripcion': 'Descripción',
            'categoria': 'Categoria',
            'monto': 'Monto',
            'fecha': 'Fecha',
            'imagen': 'Imagen',
        }
