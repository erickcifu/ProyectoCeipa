from django import forms
from app.models import Institucion

class InstitucionForm(forms.ModelForm):
    estado_ins = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = Institucion
        fields = ['nombre_ins', 'correo_ins', 'estado_ins']
        labels = {
        'nombre_ins':'Nombre de la institución',
        'correo_ins': 'Correo electrónico de la institucion',
        'estado_ins':'Activo/Inactivo',
        }
        widget = {'nombre_ins': forms.TextInput}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
