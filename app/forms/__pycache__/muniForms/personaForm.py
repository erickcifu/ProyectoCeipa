from django import forms
from app.models import Persona


class PersonaForm(forms.ModelForm):
    estado_persona = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = Persona
        fields = ['persona',
        'apellidos_persona',
        'direccion_persona',
        'telefono',
        'telefonoc',
        'cui',
        'fotografia_persona',
        'muni',
        'etni',
        'estudios_anteriores',
        'gen', 'disc','estado_persona']
        labels = {
        'persona':'Nombres',
        'apellidos_persona':'Apellidos',
        'direccion_persona':'Direcciòn',
        'telefono':'Telefono personal',
        'telefonoc':'Telefono de casa',
        'cui':'CUI',
        'fotografia_persona':'Fotografía del participante',
        'muni':'Municipio',
        'etni':'Etnia',
        'estudios_anteriores':'Ultimos grado cursado',
         'gen':'Gènero',
         'disc':' ¿Tiene alguna discapacidad?',
         'estado_persona':" Activo/inactivo"}
        widget = {'persona': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['estudios_anteriores'].empty_label = "Seleccione ultimo grado cursado"
            self.fields['muni'].empty_label = "Seleccione Municipio"
            self.fields['etni'].empty_label = "Seleccione Etnia"
            self.fields['gen'].empty_label = "Seleccione Genero"
            self.fields['disc'].empty_label = "Seleccione Discapacidad"
