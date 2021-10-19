from django import forms

from app.models import Religion_alumno, religion, Alumno


class ReligionAlumnoForm(forms.ModelForm):
    class Meta:
        model = Religion_alumno
        fields = ['religion', 'nombre_iglesia', 'estado_religionalumno']
        labels = {'nombre_iglesia':"Nombre de Iglesia", 'estado_religionalumno':"Estado"}
        widget = {'nombre_iglesia': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['religion'].empty_label = "Seleccione Religion"
