from django import forms
from django.forms import widgets
from app.models import Persona


class PersonaForm(forms.ModelForm):
    estado_persona = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo"
    )
    class Meta:
        model = Persona
        fields = ['persona',
        'apellidos_persona',
        'direccion_persona',
        'telefono_Persona',
        'telefonoc_per',
        'cui_persona',
        'fotografia_persona',
        'muni',
        'etni',
        'estudios_anteriores',
        'gen', 'disc','estado_persona']
        labels = {
        'persona':'Nombres',
        'apellidos_persona':'Apellidos',
        'direccion_persona':'Dirección domiciliar',
        'telefono_Persona':'Teléfono personal',
        'telefonoc_per':'Teléfono de casa',
        'cui_persona':'CUI',
        'fotografia_persona':'Fotografía',
        'muni':'Municipio',
        'etni':'Etnia',
        'estudios_anteriores':'Último grado cursado',
        'gen':'Género',
        'disc':' ¿Tiene alguna discapacidad?',
        'estado_persona':" Activo"}
        widget = {'persona': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'required': False
            })
            if field == 'estado_persona':
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input',
                    'checked':True
            })
            if field == 'disc':
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input',
                    'checked':False
            })
            requiered = self.fields[field].required
            if requiered:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
            })
            if field == 'telefono_Persona':
                self.fields[field].widget.attrs.update({
                    'placeholder':'00000000',
                    'onblur':'isTelephoneNumber({});'.format('id_'+field),
            })
            if field == 'telefonoc_per':
                self.fields[field].widget.attrs.update({
                    'placeholder':'00000000',
                    'onblur':'isTelephoneNumber({});'.format('id_'+field),
            })
            if field == 'cui_persona':
                self.fields[field].widget.attrs.update({
                    'placeholder':'0000 00000 0000',
                    'onblur':'isIdentify({});'.format('id_'+field),
            })
        self.fields['estudios_anteriores'].empty_label = "Seleccione último grado cursado"
        self.fields['muni'].empty_label = "Seleccione Municipio"
        self.fields['etni'].empty_label = "Seleccione Etnia"
        self.fields['gen'].empty_label = "Seleccione Género"
        self.fields['disc'].empty_label = "Seleccione Discapacidad"
