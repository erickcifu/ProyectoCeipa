from django import forms

from app.models import Religion_alumno, religion, Alumno


class ReligionAlumnoForm(forms.ModelForm):
    religion = forms.ModelChoiceField(
        queryset = religion.objects.filter(estado_religion=True)
        .order_by('nombre_religion')
    )
    alumno = forms.ModelChoiceField(
        queryset = Alumno.objects.filter(estado_alumno=True)
        .order_by('nombres_alumno')
    )

    class Meta:
        model = Religion_alumno
        fields = ['alumno', 'religion', 'nombre_iglesia', 'estado_religionalumno']
        labels = {'nombre_iglesia':"Nombre de Iglesia", 'estado_religionalumno':"Estado"}
        widget = {'nombre_iglesia': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['religion'].empty_label = "Seleccione Religion"
            self.fields['alumno'].empty_label = "Seleccione al Alumno"
