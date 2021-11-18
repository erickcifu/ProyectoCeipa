from django import forms
from app.models import PadresSociop

class PadresForm(forms.ModelForm):
    class Meta:
        model = PadresSociop
        fields = ['nombre_madre','telefono_madre', 'ocupacion_madre', 'nombre_padre', 'telefono_padre', 'ocupacion_padre', 'estado_padres']
        labels = {
            'nombre_madre':'Nombre de la madre',
            'telefono_madre':'No.Telefono de la madre',
            'ocupacion_madre':'Ocupación de la madre',
            'nombre_padre':'Nombre del padre',
            'telefono_padre':'No.Telefono del padre',
            'ocupacion_padre':'Ocupación del padre',
            'estado_padres':'Activo'}
        widget = {
            'nombre_madre': forms.TextInput,
            'estado_padres': forms.CheckboxInput(
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
            if field == 'estado_padres':
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
