from django import forms
from app.models import Curso, Grado

class CursoForm(forms.ModelForm):
    grado = forms.ModelChoiceField(
        queryset = Grado.objects.filter(estado_grado=True)
        .order_by('nombre_grado')
    )
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
            self.fields['grado'].empty_label = "Seleccione un Grado"
