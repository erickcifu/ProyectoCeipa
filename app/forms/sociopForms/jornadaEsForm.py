from django import forms
from app.models import JornadaEstudios

class JornadaesForm(forms.ModelForm):
    class Meta:
        model = JornadaEstudios
        fields = ['jornada','estado_joranadaes']
        labels = {'jornada':'Jornada de estudios','estado_joranadaes':'Activo/Inactivo'}
        widget = {
            'jornada': forms.TextInput,
            'estado_joranadaes': forms.CheckboxInput(
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
