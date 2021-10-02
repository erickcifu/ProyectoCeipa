from django import forms
from app.models import Inscripcion


class InsForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['centro_educativo','alumno', 'ciclo_grado','Fecha_inscripcion','estado_incpripsion']
        labels = {'centro_educativo':"CentroEdu", 'alumno':'Alumno','ciclo_grado':'CicloGrado','estado_incpripsion':"Estado"}
        widget = {'centro_educativo': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
