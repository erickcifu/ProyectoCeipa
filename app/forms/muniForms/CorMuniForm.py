from django import forms
from app.models import CorporacionMunicipal


class CorpMuniForm(forms.ModelForm):
    estado_corporacion = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = CorporacionMunicipal
        fields = ['comision','partido','participacion','grupo','cargo','vacuna', 'estado_corporacion']
        labels = {'comision':'Comision minicipal a la que pertenece', 'partido':'Partido político al que pertenece', 'participacion':'Participa en algun grupo', 'grupo':'Grupo en el que participa', 'cargo':'Cargo que ocupa enel grupo', 'vacuna':'Vacunado contra COVID19', 'estado_corporacion':"Estado"}
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
