from django import forms
from app.models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre_curso', 'descripcion_curso', 'grado', 'estado_curso']
        labels = {'nombre_curso':'Curso', 'descripcion_curso':'Descripcion', 'grado':'Grado', 'estado_curso':'Estado'}
        widget = {'nombre_curso', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })