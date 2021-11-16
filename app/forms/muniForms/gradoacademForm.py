from django import forms
from app.models import GradoAcademico

class gradoacadForm(forms.ModelForm):
    estado_academico = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = GradoAcademico
        fields = ['nombre_academico', 'descripcion_academico', 'estado_academico']
        label = {
            'nombre_academico':'Nombre del grado académico',
            'descripcion_academico':'Descripción',
            'estado_academico':'Activo',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
