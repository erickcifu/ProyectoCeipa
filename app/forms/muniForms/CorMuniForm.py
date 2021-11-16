from django import forms
from app.models import CorporacionMunicipal


class CorpMuniForm(forms.ModelForm):
    estado_corporacion = forms.BooleanField()
    class Meta:
        model = CorporacionMunicipal
        fields = ['comision',
        'partido',
        'partido_actual',
        'correo_corporacion',
        'participacion',
        'grupo',
        'cargo','vacuna_corp', 'estado_corporacion']
        labels = {'comision':'Comision a la que pertenece',
        'partido':'Partido político con el que entró a la corporación',
        'partido_actual':'Partido político actual',
        'participacion':'Participa en algun grupo',
        'correo_corporacion':'Correo electrónico',
        'grupo':'Grupo en el que participa',
        'cargo':'Cargo que ocupa en el grupo',
        'vacuna_corp':'Vacunado contra COVID-19',
        'estado_corporacion':"Activo"}
        widget = {'comision': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'requiered':False
            })
            if field == 'estado_corporacion':
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input',
                    'checked':True
            })
            if type(self.fields[field])==forms.EmailField:
                self.fields[field].widget.attrs.update({
                    'onblur':'isEmail({});'.format('id_'+field)
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
        self.fields['comision'].empty_label = "Seleccione una comision"
        self.fields['partido'].empty_label = "Seleccione un partido"
        self.fields['grupo'].empty_label = "Seleccione un grupo"
        self.fields['cargo'].empty_label = "Seleccione cargo"
