from django import forms
from app.models import OcupacionTutor

class OcupTutorForm(forms.ModelForm):
    class Meta:
        model = OcupacionTutor
        fields = ['ocupacion_tutor','estado_ocuptutor']
        labels = {'ocupacion_tutor':'Ocupación','estado_ocuptutor':'Activo/Inactivo'}
        widget = {
            'ocupacion_tutor': forms.TextInput,
            'estado_ocuptutor': forms.CheckboxInput(
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
