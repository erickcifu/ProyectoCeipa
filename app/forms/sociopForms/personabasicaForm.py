from django import forms
from app.models import PersonaBasica

class PersonaBForm(forms.ModelForm):
    class Meta:
        model = PersonaBasica
        fields = [
            'nombresp',
            'apellidos',
            'fecha_nacimiento',
            'DPIP',
            'direccion',
            'tel_casa',
            'tel_cel',
            'email',
            'cantidad_convivientes',
            'conquien_vive',
            'fotografiaP',
            'municipio',
            'etnia',
            'genero',
            #'vivienda_socio',
            'info_educacion',
            #'caracteristicas_laborales',
            'aspectos_salud',
            'razon',
            #'info_economica',
            'ingreso_total',
            'total_gastos',
            'edad',
            #'tutor_socio',
            'padres',
            'estado_persona_basica'
            ]

        labels = {
            'nombres':'Nombres',
            'apellidos':'Apellidos',
            'fecha_nacimiento':'Fecha de nacimiento',
            'DPI_CUI':'DPI/CUI',
            'direccion':'Dirección',
            'tel_casa':'Teléfono de casa',
            'tel_cel':'Teléfono Celular',
            'email':'Email',
            'cantidad_convivientes':'Cantidad de Convivientes',
            'conquien_vive':'Con quien vive',
            'fotografia':'Fotografía',
            'municipio':'Municipio',
            'etnia':'Etnia',
            'genero':'Género',
            #'vivienda_socio':'Vivienda',
            'info_educacion':'Información de Educación',
            #'caracteristicas_laborales':'Caracteristicas Laborales',
            'aspectos_salud':'Aspectos de Salud',
            'razon':'Razón',
            #'info_economica':'Información Económica',
            'ingreso_total':'Ingreso Total',
            'total_gastos':'Total de Gastos',
            'edad':'Edad',
            #'tutor_socio':'Tutor',
            'padres':'Padres',
            'estado_persona_basica':'Activo/Inactivo'}
        widget = {
            'nombres': forms.TextInput,
            'estado_persona_basica': forms.CheckboxInput(
                attrs = {
                    'checked':True,
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
