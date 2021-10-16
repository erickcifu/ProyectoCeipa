from django import forms
from app.models import ComisionNA

class Comision_NAForm(forms.ModelForm):
    estado_comision = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = ComisionNA
        fields = ['institucion', 'participacion', 'estado_comision']
        labels = {
        'institucion':'Nombre de la institución a la que pertenece',
        'participacion':'Participación dentro del grupo',
        'estado_comision':'Activo/Inactivo',
        }
        widget = {'nombre_grupo': forms.TextInput}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
