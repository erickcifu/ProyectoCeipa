from django import forms
from app.models import Tipo_medio

class TmedioForm(forms.ModelForm):
    class Meta:
        model = Tipo_medio
        fields = ['tipo_medio', 'estado_tmedio']
        labels = {'tipo_medio':'Tipo de medio de comunicación', 'estado_tmedio':"Activo/Inactivo"}
        widget = {'tipo_medio': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
