from django import forms
from app.models import ProgramaC

class ProgramaCForm(forms.ModelForm):
    estado_programa = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = ProgramaC
        fields = ['nombre_programa', 'estado_programa']
        labels = {
        'nombre_programa':'Nombre del programa',
        'estado_programa':'Activo',
        }
        widget = {'nombre_programa': forms.TextInput}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
