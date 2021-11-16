from django import forms
from django.forms import widgets
from app.models import Beneficiado


class BenForm(forms.ModelForm):
    fecha_nacimiento_benef = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        ), label = 'Fecha de nacimiento'
    )
    estado_beneficiado = forms.BooleanField()
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
        'estado_beneficiado':"Activo"}
        widget = {'estado_beneficiado': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'required': False
            })
            if field == 'estado_beneficiado':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input',
                'checked':True,
            })
            if field == 'establecimiento_privado':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input',
                'checked':False,
            })

            if field=='establecimiento_publico':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input',
                'checked':False,
            })
            if field=='establecimiento_publico':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input',
                'checked':False,
            })
            if field=='nivel_primario' or field=='nivel_secundario' or field=='nivel_universitario':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input',
                'checked':False,
            })
            requiered = self.fields[field].required
            if requiered:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
                })
            if field == 'fecha_nacimiento_benef':
                self.fields[field].widget.attrs.update({
                    'placeholder':'dd/mm/yyyy',
                    'type':'date'
                })
            self.fields['ocup'].empty_label = "Seleccione ocupación"
