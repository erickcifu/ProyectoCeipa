from django import forms
from app.models import Maestro

class MaestroForm(forms.ModelForm):
    estado_maestro = forms.BooleanField()
    class Meta:
        model = Maestro
        fields = ['establecimiento',
        'area_rural',
        'area_urbana',
        'est_publico',
        'est_privado',
        'participa_maestro',
        'correo_maestro',
        'gruporg',
        'cargogrup',
        'estado_maestro'
        ]

        labels = {'establecimiento':'Nombre del establecimiento',
        'area_rural':'Rural',
        'area_urbana':'Urbana',
        'est_publico':'Público',
        'est_privado':'Privado',
        'participa_maestro':'¿Participa en algun grupo organizado?',
        'correo_maestro':'Correo electrónico',
        'gruporg':'Cargo en el grupo organizado',
        'cargogrup':'Grupo organizado al que pertenece',
        'estado_maestro':"Activo"}
        widget = {'establecimiento': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'requiered':False
            })
            if field == 'estado_maestro':
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
        self.fields['establecimiento'].empty_label = "Seleccione un Establecimiento"
        self.fields['gruporg'].empty_label = "Seleccione su cargo"
        self.fields['cargogrup'].empty_label = "Seleccione grupo"
