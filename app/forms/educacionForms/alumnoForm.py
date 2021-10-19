from django import forms
from app.models import Alumno, municipio, genero

class AlumnoForm(forms.ModelForm):

    fecha_nacimiento = forms.DateField()
    estado_alumno = forms.BooleanField()
    class Meta:
        model = Alumno
        fields = ['nombres_alumno', 'apellidos_alumno', 'cui','edad', 'codigo_mineduc', 'fecha_nacimiento', 'muni', 'ingreso_familiar', 'direccion_alumno', 'telefono', 'fotografia', 'ocup', 'gen', 'etni', 'idiome',  'estado_alumno']
        labels = {'nombres_alumno':'Nombres',
            'apellidos_alumno':'Apellidos',
            'cui':"CUI",
            'codigo_mineduc':'Codigo Mineduc',
            'fecha_nacimiento':'Fecha de nacimiento',
            'ingreso_familiar':"Ingreso Familiar",
            'direccion_alumno':"Direccion",
            'telefono':"Telefono",
            'fotografia':"Fotografia",
            'ocup':"Ocupacion",
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
        #self.fields['municipio'].empty_label = "Seleccione municipio"
        #self.fields['genero'].empty_label = "Seleccione Genero"
        self.fields['ocup'].empty_label = "Seleccione ocupacion"
        self.fields['etni'].empty_label = "Seleccione etnia"
        self.fields['idiome'].empty_label = "Seleccione ocupacion"
