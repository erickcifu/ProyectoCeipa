from django import forms
from app.models import Maestro

class MaestroForm(forms.ModelForm):
    estado_maestro = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = Maestro
        fields = ['establecimiento', 'gruporg', 'cargogrup', 'estado_maestro']
        labels = {'establecimiento':'Establecimiento', 'estado_maestro':"Estado"}
        widget = {'persona': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['establecimiento'].empty_label = "Seleccione un Establecimiento"
            self.fields['gruporg'].empty_label = "Seleccione su Grupo Organizado"
            self.fields['cargogrup'].empty_label = "Seleccione su Cargo Grupo"
