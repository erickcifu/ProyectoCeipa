from django import forms
from app.models import Beneficiado


class BenForm(forms.ModelForm):
    estado_beneficiado = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = Beneficiado
        fields = ['ocup', 'establecimiento', 'estado_beneficiado']
        labels = {'ocup':'Ocupación','establecimiento':'Establecimiento donde estudia','estado_beneficiado':"Activo/Inactivo"}
        widget = {'estado_beneficiado': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['ocup'].empty_label = "Seleccione su ocupacion"
            self.fields['establecimiento'].empty_label = "Seleccione su establecimiento"
            self.fields['ocup'].required = False
