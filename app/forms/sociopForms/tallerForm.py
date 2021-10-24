from django import forms
from app.models import Taller

class TallerForm(forms.ModelForm):
    class Meta:
        model = Taller
        fields = ['nombre_taller', 'descripcion_taller', 'estado_taller']
        labels = {'nombre_taller':'Nombre de Taller', 'descripcion_taller':'Descripcion del Taller', 'estado_taller':'Activo/Inactivo'}
        widget = {
            'nombre_taller': forms.TextInput,
            'estado_taller': forms.CheckboxInput(
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
