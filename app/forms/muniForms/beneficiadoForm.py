from django import forms
from app.models import Beneficiado


class BenForm(forms.ModelForm):
    fecha_nacimiento_benef = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    estado_beneficiado = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = Beneficiado
        fields = ['ocup',
        'fecha_nacimiento_benef',
        'establecimiento',
        'establecimiento_privado',
        'establecimiento_publico',
        'nivel_primario',
        'nivel_secundario',
        'nivel_universitario',
        'estado_beneficiado']
        labels = {'ocup':'Ocupación del beneficiado',
        'fecha_nacimiento':'Fecha de nacimiento',
        'establecimiento':'Nombre del establecimiento donde estudia',
        'establecimiento_privado':'Privado',
        'establecimiento_publico':'Público',
        'nivel_primario':'Primaria',
        'nivel_secundario':'Secundaria',
        'nivel_universitario':'Universidad',
        'estado_beneficiado':"Activo/Inactivo"}
        widget = {'estado_beneficiado': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['ocup'].empty_label = "Seleccione ocupacion"
            self.fields['ocup'].required = False
