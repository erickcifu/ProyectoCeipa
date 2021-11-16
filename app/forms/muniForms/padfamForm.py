from django import forms
from app.models import PadresFamilia

class PadFamForm(forms.ModelForm):
    estado_padres = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = PadresFamilia
        fields = ['leer_P', 'escribir_p',
        'cantidad_hijos','programaC',
        'vacunaCovid','correo_padres',
        'participacionG', 'grupo',
         'cargo','estado_padres']
        labels = {'leer_P':'Sabe leer',
        'escribir_p':'Sabe escribir',
        'cantidad_hijos':'Cantidad de hijos que tiene',
        'programaC':'Programa al que pertenece en CEIPA',
        'vacunaCovid':'Està vacunado contra COVID-19',
        'correo_padres':'Correo electrónico',
        'participacionG':'Ha participado en algùn grupo organizado',
        'grupo':'Grupo en el que ha participado',
        'cargo':'Cargo que ha ocupado',
        'estado_padres':"Activo"}
        widget = {
        'grupo': forms.TextInput,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['grupo'].empty_label = "Seleccione grupo"
            self.fields['cargo'].empty_label = "Seleccione cargo"
            self.fields['programaC'].empty_label = "Seleccione un Programa Ceipa"
