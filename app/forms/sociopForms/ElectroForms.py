from django import forms
from app.models import Electrodomesticos

class ElectroForm(forms.ModelForm):
    estado_electro = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = Electrodomesticos
        fields = ['Nombre_electro', 'estado_electro']
        labels = {'Nombre_electro':'Nombre de Electrodomestico','estado_electro':'Activo/Inactivo'}
        widget = {
            'Nombre_electro': forms.TextInput,
            'estado_electro': forms.CheckboxInput(
                attrs = {
                    'checked':True,
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
