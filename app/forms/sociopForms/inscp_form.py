from django import forms
from app.models import Taller, PersonaBasica, Inscripcionp
from app.models.educacion_model.municipioModel import municipio

class InscpForm(forms.ModelForm):
    insc_persona = forms.ModelChoiceField(
        queryset = PersonaBasica.objects.filter(estado_persona_basica=True)
        .order_by('nombresp'), label="Participante"
    )
    lugar_inscripcion = forms.ModelChoiceField(
        queryset = municipio.objects.filter(estado_municipio=True)
        .order_by('nombre_municipio'), label="Lugar de inscrićión"
    )
    taller = forms.ModelChoiceField(
        queryset = Taller.objects.filter(estado_taller=True)
        .order_by('nombre_taller')
    )

    inicio_taller = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    final_taller = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    class Meta:
        model = Inscripcionp
        fields = [
            'insc_persona',
            'taller',
            'lugar_inscripcion',
            'inicio_taller',
            'final_taller',
            'certificado_taller',
            ]
        labels = {
            'insc_persona':'Participante',
            'taller':'Nombre del taller',
            'lugar_inscripcion':'Lugar de inscripción',
            'inicio_taller':'Fecha de inicio de taller',
            'final_taller':'Fecha de finalización de taller',
            'certificado_taller':'Tiene certificado',
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['taller'].empty_label = "Seleccione taller"
            self.fields['lugar_inscripcion'].empty_label = "Seleccione municipio"

class InscTallerForm(forms.ModelForm):
    insc_persona = forms.ModelChoiceField(
        queryset = PersonaBasica.objects.filter(estado_persona_basica=True)
        .order_by('nombresp'), label="Participante"
    )
    lugar_inscripcion = forms.ModelChoiceField(
        queryset = municipio.objects.filter(estado_municipio=True)
        .order_by('nombre_municipio'), label="Lugar de inscripción"
    )

    inicio_taller = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        ), label = "Fecha de inicio del taller"
    )
    final_taller = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        ), label = "Fecha de finalización del taller"
    )
    class Meta:
        model = Inscripcionp
        fields = ['insc_persona',
            'lugar_inscripcion',
            'inicio_taller',
            'final_taller',]
        labels = {
            'insc_persona':'Participante',
            'lugar_inscripcion':'Lugar de inscripción',
            'inicio_taller':'Fecha de inicio de taller',
            'final_taller':'Fecha de finalización de taller',
        }
        widget = {'insc_persona': forms.TextInput,}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'required':False
            })
        self.fields['insc_persona'].empty_label = "Seleccione al participante"
        self.fields['lugar_inscripcion'].empty_label = "Seleccione municipio"
