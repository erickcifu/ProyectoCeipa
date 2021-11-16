from django import forms
from app.models import TutorMuni

class TutorMuniForm(forms.ModelForm):
    fecha_nacimiento_T = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        ), label = 'Fecha de nacimiento'
    )
    estado_tutor = forms.BooleanField()
    class Meta:
        model = TutorMuni
        fields = ['nombres_tutor', 'apellidos_tutor',
        'parentesco','DPI_T',
        'fecha_nacimiento_T', 'direccion_tutor',
        'telefono_T', 'fotografia_tutor', 'estado_tutor']
        labels = {'nombres_tutor':'Nombres',
        'apellidos_tutor':'Apellidos',
        'parentesco':'Parentesco que tiene con el beneficiado',
        'DPI_T':"No. DPI",
        'fecha_nacimiento_T':'Fecha de nacimiento',
        'direccion_tutor':'Direccion',
        'telefono_T':"No. Telefono",
        'fotografia_tutor':"Fotografia",
        'estado_tutor':'Activo'}
        widget = {'nombres_tutor', forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'required': False
            })
            if field == 'estado_tutor':
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input',
                    'checked':True
            })
            requiered = self.fields[field].required
            if requiered:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
            })
            if field == 'telefono_T':
                self.fields[field].widget.attrs.update({
                    'placeholder':'00000000',
                    'onblur':'isTelephoneNumber({});'.format('id_'+field),
            })
            if field == 'DPI_T':
                self.fields[field].widget.attrs.update({
                    'placeholder':'0000 00000 0000',
                    'onblur':'isIdentify({});'.format('id_'+field),
            })
            if field == 'fecha_nacimiento_T':
                self.fields[field].widget.attrs.update({
                    'placeholder':'dd/mm/yyyy',
                    'type':'date'
                })
        self.fields['parentesco'].empty_label = "Seleccione parentesco con el participante"
