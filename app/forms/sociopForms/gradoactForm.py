from django import forms
from app.models import Grado_actual

class GradoactForm(forms.ModelForm):
    class Meta:
        model = Grado_actual
        fields = ['gradoact','estado_gradoact']
        labels = {'gradoact':'Nombre del grado','estado_gradoact':'Activo/Inactivo'}
        widget = {
            'gradoact': forms.TextInput,
            'estado_gradoact': forms.CheckboxInput(
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
