from django import forms
from app.models import Establecimiento


class EstablecimientoForm(forms.ModelForm):
    class Meta:
        model = Establecimiento
        fields = ['nombre_establecimiento',
        'direccion_estable', 'estado_estable']
        labels = {'nombre_establecimiento':"Establecimiento",
         'direccion_estable':"Direccion",
         'estado_estable':"Estado"}
        widget = {'nombre_establecimiento': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
