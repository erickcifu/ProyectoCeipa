from django import forms
from app.models import AusenBeneficiado, Area, Beneficiado

class AusenBeneficiadoForm(forms.ModelForm):
    area = forms.ModelChoiceField(
        queryset = Area.objects.filter(estado_area=True)
        .order_by('nombre_area')
    )
    beneficiado = forms.ModelChoiceField(
        queryset = Beneficiado.objects.filter(estado_beneficiado=True)
        .order_by('id')
    )
    class Meta:
        model = AusenBeneficiado
        fields = ['observaciones', 'fecha', 'area', 'beneficiado', 'estado']
        labels = {'observaciones':'Observaciones', 'fecha':'Fecha', 'area':"Area", 'beneficiado':'Beneficiado', 'estado':'Estado'}
        widget = {'observaciones', forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['area'].empty_label = "Seleccione Area"
        self.fields['beneficiado'].empty_label = "Seleccione Beneficiado"