from django import forms
from app.models import Alumno, municipio, genero

class AlumnoForm(forms.ModelForm):
    municipio = forms.ModelChoiceField(
        queryset = municipio.objects.filter(estado_municipio=True)
        .order_by('nombre_municipio')
    )
    genero = forms.ModelChoiceField(
        queryset = genero.objects.filter(estado_genero=True)
        .order_by('genero')
    )

    class Meta:
        model = Alumno
        fields = ['nombres_alumno', 'apellidos_alumno', 'cui', 'codigo_mineduc', 'fecha_nacimiento', 'ingreso_familiar', 'direccion_alumno', 'telefono', 'fotografia', 'ocup', 'tutor', 'etni', 'idiome', 'estudios_anteriores', 'muni', 'gen', 'estado_alumno']
        labels = {'nombres_alumno':'Nombres',
            'apellidos_alumno':'Apellidos',
            'cui':"cui",
            'codigo_mineduc':'Codigo Mineduc',
            'fecha_nacimiento':'Fecha de nacimiento',
            'ingreso_familiar':"Ingreso Familiar",
            'direccion_alumno':"Direccion",
            'telefono':"Telefono",
            'fotografia':"Fotografia",
            'ocup':"Ocupacion",
            'tutor':"Tutor",
            'etni':"Etnia",
            'idiome':"Idioma",
            'estudios_anteriores':"Estudios Anteriores",
            'muni':"Municipalidad",
            'gen':"Genero",
            'estado_conviviente':'Estado'
        }

        widget = {'nombres_alumno', forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['municipio'].empty_label = "Seleccione municipio"
        self.fields['genero'].empty_label = "Seleccione Genero"
