from django import forms
from app.models import GrupoNA

class GrupoNAForm(forms.ModelForm):
    class Meta:
        model = GrupoNA
        fields = ['nombre_grupona','estado_grupona']
        labels = {'nombre_grupona':'Nombre del grupo','estado_grupona':'Activo/Inactivo'}
        widget = {
            'nombre_grupona': forms.TextInput,
            'estado_grupona': forms.CheckboxInput(
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
