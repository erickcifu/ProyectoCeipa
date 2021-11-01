from django import forms
from app.models import Maestro

class MaestroForm(forms.ModelForm):
    estado_maestro = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
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

        labels = {'establecimiento':'Establecimiento',
        'area_rural':'Rural',
        'area_urbana':'Urbana',
        'est_publico':'Público',
        'est_privado':'Privado',
        'participa_maestro':'¿Participa en algun grupo organizado?',
        'correo_maestro':'Correo electrónico',
        'gruporg':'Cargo en el grupo organizado',
        'cargogrup':'Grupo organizado al que pertenece',
        'estado_maestro':"Activo/Inactivo"}
        widget = {'establecimiento': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['establecimiento'].empty_label = "Seleccione un Establecimiento"
            self.fields['gruporg'].empty_label = "Seleccione su cargo"
            self.fields['cargogrup'].empty_label = "Seleccione grupo"
