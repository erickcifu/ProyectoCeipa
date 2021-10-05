from django import forms
from app.models import BeneficiadoArea

class BenefArForm(forms.ModelForm):
    class Meta:
        model = BeneficiadoArea
        fields = ['area', 'programa', 'beneficiado', 'observacion','fecha', 'estado_ba']
        labels = {'area':'Area', 'programa':'programa', 'beneficiado':'Beneficiado', 'estado_ba':"Estado"}
        widget = {'beneficiado': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['area'].empty_label = "Seleccione a la Persona"
            self.fields['programa'].empty_label = "Seleccione un grupo"
            self.fields['beneficiado'].empty_label = "Seleccione a la cargo"
