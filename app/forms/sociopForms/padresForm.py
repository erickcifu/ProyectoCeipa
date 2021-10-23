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
            'estado_joranadaes':'Activo/Inactivo'}
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
                'class':'form-control'
            })
            self.fields['nombre_madre'].required = False
            self.fields['telefono_madre'].required = False
            self.fields['ocupacion_madre'].required = False
            self.fields['nombre_padre'].required = False
            self.fields['telefono_padre'].required = False
            self.fields['ocupacion_padre'].required = False
