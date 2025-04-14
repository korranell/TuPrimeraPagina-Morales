from django import forms
from .models import Transaccion
from django.contrib.auth.models import User

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['fecha', 'categoria', 'monto', 'descripcion', 'usuario']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'usuario': forms.Select(attrs={'class': 'form-select'}), 
        }

    def __init__(self, *args, **kwargs):
        super(TransaccionForm, self).__init__(*args, **kwargs)
        if 'usuario' in self.fields:
            self.fields['usuario'].queryset = User.objects.all()  
            self.fields['usuario'].initial = None  