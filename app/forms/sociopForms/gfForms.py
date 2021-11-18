from django import forms
from app.models import GastoFamiliar

class GastFamForm(forms.ModelForm):
    class Meta:
        model = GastoFamiliar
        fields = ['servicio', 'cantidad_servicio', 'estado_gastofamiliar']
        labels = {'servicio':'Nombre del servicio', 'cantidad_servicio':'Cantidad mensual por servicio', 'estado_gastofamiliar':'Activo'}
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
                'class':'form-control',
                'required':False
            })
            if field == 'estado_gastofamiliar':
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input',
                    'checked':True
            })
            if type(self.fields[field])==forms.BooleanField:
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input'
            })
            requiered = self.fields[field].required
            if requiered:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
            })
