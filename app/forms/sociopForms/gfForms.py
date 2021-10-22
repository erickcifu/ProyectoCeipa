from django import forms
from app.models import GastoFamiliar

class GastFamForm(forms.ModelForm):
    class Meta:
        model = GastoFamiliar
        fields = ['servicio', 'cantidad_servicio', 'estado_gastofamiliar']
        labels = {'servicio':'Nombre servicio', 'cantidad_servicio':"Cantidad por servicio",'estado_gastofamiliar':'Activo/Inactivo'}
        widget = {
            'servicio': forms.TextInput,
            'estado_gastofamiliar': forms.CheckboxInput(
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
