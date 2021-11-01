from django import forms
from app.models import Alumno, municipio, genero


class AlumnoForm(forms.ModelForm):

    fecha_nacimiento = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    estado_alumno = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    edad = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'hidden':True,
            }
        ), required=False
    )
    class Meta:
        model = Alumno
        fields = ['ocup','nombres_alumno', 'apellidos_alumno', 'cui','edad', 'codigo_mineduc', 'fecha_nacimiento', 'muni', 'ingreso_familiar', 'direccion_alumno', 'telefono', 'fotografia', 'gen', 'etni', 'idiome',  'estado_alumno']
        labels = {
            'ocup':'Ocupacion',
            'nombres_alumno':'Nombres',
            'apellidos_alumno':'Apellidos',
            'cui':"CUI",
            'codigo_mineduc':'Codigo Mineduc',
            'fecha_nacimiento':'Fecha de nacimiento',
            'ingreso_familiar':"Ingreso Familiar",
            'direccion_alumno':"Direccion",
            'telefono':"Telefono",
            'fotografia':"Fotografia",
            'etni':"Etnia",
            'idiome':"Idioma que habla",
            'gen':'Genero',
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
                'class':'form-control'
            })
        self.fields['ocup'].empty_label = "Seleccione ocupación"
        self.fields['etni'].empty_label = "Seleccione etnia"
        self.fields['idiome'].empty_label = "Seleccione idioma"
        self.fields['nombres_alumno'].required = False
        self.fields['apellidos_alumno'].required = False
