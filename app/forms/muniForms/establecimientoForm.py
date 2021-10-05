from django import forms
from app.models import Establecimiento


class EstablecimientoForm(forms.ModelForm):
    class Meta:
        model = Establecimiento
        fields = ['nombre_establecimiento', 'direccion', 'estado']
        labels = {'nombre_establecimiento':"Establecimiento", 'direccion':"Direccion", 'estado':"Estado"}
        widget = {'nombre_establecimiento': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })