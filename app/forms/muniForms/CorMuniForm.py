from django import forms
from app.models import CorporacionMunicipal


class CorpMuniForm(forms.ModelForm):
    class Meta:
        model = CorporacionMunicipal
        fields = ['comision','partido','participacion','grupo','cargo','vacuna', 'estado_corporacion']
        labels = {'persona':'Nombres', 'comision':'comision', 'partido':'partido', 'participacion':'participacion', 'grupo':'grupo', 'cargo':'cargo', 'vacuna':'vacuna', 'estado_corporacion':"Estado"}
        widget = {'comision': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['comision'].empty_label = "Seleccione una comision"
            self.fields['partido'].empty_label = "Seleccione un partido"
            self.fields['grupo'].empty_label = "Seleccione un grupo"
            self.fields['cargo'].empty_label = "Seleccione cargo"
