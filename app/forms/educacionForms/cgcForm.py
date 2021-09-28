from django import forms
from app.models import Ciclo_grado_curso

class CGCForm(forms.ModelForm):
    class Meta:
        model = Ciclo_grado_curso
        fields = ['maestro', 'curso', 'ciclo_grado','estado_cgc']
        labels = {'maestro':'Maestro','ciclo_grado':'CicloG', 'curso':'Curso', 'estado_cgc':'Estado'}
        widget = {'maestro', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
