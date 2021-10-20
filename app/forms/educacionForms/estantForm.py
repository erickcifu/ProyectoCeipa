from django import forms
from app.models import EstudiosAnt

class EstAntForm(forms.ModelForm):
    estado_estudiosant = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = EstudiosAnt
        fields = ['grado','nombre_establecimiento', 'telefono','repitente','estado_estudiosant']
        labels = {'nombre_establecimiento':"Establecimiento anterior", 'repitente':"Repitente",'estado_estudiosant':"Estado"}
        widget = {'nombre_establecimiento': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['grado'].empty_label = "Seleccione un Grado"
