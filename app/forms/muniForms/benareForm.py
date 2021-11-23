from django import forms
from app.models import BeneficiadoArea
from app.models import Area

class BenefArForm(forms.ModelForm):
    fecha_ba = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        ), label="Fecha de inscripción"
    )
    class Meta:
        model = BeneficiadoArea
        fields = [
        'programa',
        'beneficiado',
        'observacion',
        'fecha_ba',
        'estado_ba',
        ]
        labels = {
        'programa':'programa',
        'beneficiado':'Participante',
        'fecha_ba':'Fecha de inscripción',
        'observacion':'Observaciones',
        'estado_ba':"Activo"}
        widget = {'beneficiado': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['programa'].empty_label = "Programa al que pertenece en CEIPA"
            self.fields['beneficiado'].empty_label = "Seleccione al participante"

class BenefAr_EditForm(forms.ModelForm):
    class Meta:
        model = BeneficiadoArea
        fields = ['programa', 'beneficiado', 'observacion','fecha_ba', 'estado_ba']
        labels = {'area':'Area', 'programa':'programa', 'beneficiado':'Beneficiado', 'fecha_ba':'Fecha','estado_ba':"Estado"}
        widget = {'beneficiado': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['programa'].empty_label = "Programa al que pertenece en CEIPA"
            self.fields['beneficiado'].empty_label = "Seleccione al beneficiado"
