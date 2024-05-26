from django import forms
from .models import Ponte, Barra

class PonteForm(forms.ModelForm):
    class Meta:
        model = Ponte
        fields = ['nome_ponte']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        

class BarraForm(forms.ModelForm):
    class Meta:
        model = Barra
        fields = ['nome_barra', 'cm', 'esforco_interno', 'tipo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'