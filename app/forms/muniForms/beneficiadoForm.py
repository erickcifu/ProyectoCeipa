from django import forms
from app.models import Beneficiado


class BenForm(forms.ModelForm):
    class Meta:
        model = Beneficiado
        fields = ['gen', 'ocup', 'establecimiento', 'estado_beneficiado']
        labels = {'gen':'Genero', 'ocup':'ocupacion','establecimiento':'establecimiento','estado_beneficiado':"Estado"}
        widget = {'estado_beneficiado': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['gen'].empty_label = "Seleccione su Genero"
            self.fields['ocup'].empty_label = "Seleccione su ocupacion"
            self.fields['establecimiento'].empty_label = "Seleccione su establecimiento"
