from django import forms
from django.forms import widgets
from app.models import Alumno, municipio, genero


class AlumnoForm(forms.ModelForm):

    fecha_nacimiento = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    estado_alumno = forms.BooleanField()
    edad = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'hidden':True,
            }
        ), required=False
    )
    class Meta:
        model = Alumno
        fields = [
            'ocup',
            'nombres_alumno',
            'apellidos_alumno',
            'cui','edad',
            'codigo_mineduc',
            'fecha_nacimiento',
            'muni', 'ingreso_familiar',
            'direccion_alumno',
            'telefono_alumno',
            'fotografia',
            'gen', 'etni',
            'idiome',  'estado_alumno'
        ]
        labels = {
            'ocup':'Ocupación',
            'nombres_alumno':'Nombres',
            'apellidos_alumno':'Apellidos',
            'cui':"CUI",
            'codigo_mineduc':'Codigo Mineduc',
            'fecha_nacimiento':'Fecha de nacimiento',
            'ingreso_familiar':"Ingreso Familiar",
            'direccion_alumno':"Direccion",
            'telefono_alumno':"Telefono",
            'fotografia':"Fotografia",
            'etni':"Grupo étnico",
            'idiome':"Idioma que habla",
            'gen':'Género',
            'muni':'Municipio',
            'estado_alumno':'Estado',
            'edad':'Edad'
        }

        widget = {'nombres_alumno', forms.TextInput,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'required': False
            })
            if field == 'estado_alumno':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input',
                'checked':True
            })
            required = self.fields[field].required
            if required:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
                })

            if field == 'telefono_alumno':
                self.fields[field].widget.attrs.update({
                    'placeholder':'45002585',
                    'onblur':'isTelephoneNumber({});'.format('id_'+field),
                })

            if field == 'cui':
                self.fields[field].widget.attrs.update({
                    'placeholder':'0000 00000 0000',
                    'onblur':'isIdentify({});'.format(field),
                })
            if field == 'fecha_nacimiento':
                self.fields[field].widget.attrs.update({
                    'placeholder':'dd/mm/yyyy',
                    'type':'date',
                })
        self.fields['ocup'].empty_label = "Seleccione ocupación"
        self.fields['etni'].empty_label = "Seleccione etnia"
        self.fields['idiome'].empty_label = "Seleccione idioma"
        self.fields['nombres_alumno'].required = False
        self.fields['apellidos_alumno'].required = False
