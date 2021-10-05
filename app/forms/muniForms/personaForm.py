from django import forms
from app.models import Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['persona', 'apellidos_persona', 'fotografia','muni', 'etni', 'estudios_anteriores', 'gen', 'disc','estado_persona']
        labels = {'persona':'Persona', 'muni':'Muni', 'etni':'etnia', 'estudios_anteriores':'estudiosAnteriores', 'estado_persona':"Estado"}
        widget = {'persona': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['estudios_anteriores'].empty_label = "Seleccione su centro anterior"
            self.fields['muni'].empty_label = "Seleccione Municipio"
            self.fields['etni'].empty_label = "Seleccione Etnia"
            self.fields['gen'].empty_label = "Seleccione Genero"
            self.fields['disc'].empty_label = "Seleccione Discapacidad"