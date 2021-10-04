from django import forms
from app.models import Maestro

class MaestroForm(forms.ModelForm):
    class Meta:
        model = Maestro
        fields = ['establecimiento', 'persona',  'gruporg', 'cargogrup', 'estado_maestro']
        labels = {'persona':'persona','establecimiento':'Establecimiento', 'estado_maestro':"Estado"}
        widget = {'persona': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['establecimiento'].empty_label = "Seleccione un Establecimiento"
            self.fields['persona'].empty_label = "Seleccione a la Persona"
            self.fields['gruporg'].empty_label = "Seleccione su Grupo Organizado"
            self.fields['cargogrup'].empty_label = "Seleccione su Cargo Grupo"
