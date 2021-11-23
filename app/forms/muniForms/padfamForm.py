from django import forms
from app.models import PadresFamilia

class PadFamForm(forms.ModelForm):
    estado_padres = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo"
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
        'vacunaCovid':'Está vacunado contra COVID-19',
        'correo_padres':'Correo electrónico',
        'participacionG':'Ha participado en algún grupo organizado',
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
                'class':'form-control',
                'required':False
            })
            if type(self.fields[field])==forms.BooleanField:
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input'
            })
            requiered = self.fields[field].required
            if requiered:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
            })
            if type(self.fields[field])==forms.EmailField:
                self.fields[field].widget.attrs.update({
                    'onblur':'isEmail({});'.format('id_'+field)
            })
        self.fields['grupo'].empty_label = "Seleccione grupo"
        self.fields['cargo'].empty_label = "Seleccione cargo"
        self.fields['programaC'].empty_label = "Seleccione un Programa Ceipa"
