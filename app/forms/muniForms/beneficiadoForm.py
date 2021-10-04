from django import forms
from app.models import Beneficiado


class BenForm(forms.ModelForm):
    class Meta:
        model = Beneficiado
        fields = ['tutor', 'persona', 'gen', 'ocup', 'estudios_anteriores', 'estado_beneficiado']
        labels = {'tutor':"tutor", 'persona':'persona', 'estado_beneficiado':"Estado"}
        widget = {'estado_beneficiado': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['tutor'].empty_label = "Seleccione su Tutor"
            self.fields['persona'].empty_label = "Seleccione a la Persona"
            self.fields['gen'].empty_label = "Seleccione su Genero"
            self.fields['ocup'].empty_label = "Seleccione su ocupacion"
            self.fields['estudios_anteriores'].empty_label = "Seleccione una institucion"
