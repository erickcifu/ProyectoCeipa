from django import forms
from app.models import PersonaBasica

class PersonaBForm(forms.ModelForm):
    fecha_nacimientop = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    class Meta:
        model = PersonaBasica
        fields = [
            'nombresp',
            'apellidosp',
            'fecha_nacimientop',
            'DPIP',
            'direccionp',
            'tel_casap',
            'tel_celp',
            'emailp',
            'cantidad_convivientesp',
            'conquien_vive',
            'fotografiaP',
            'municipio',
            'etnia',
            'genero',
            'razon',
            'ingreso_total',
            'total_gastos',
            'edad',
            'estado_persona_basica'
            ]

        labels = {
            'nombresp':'Nombres',
            'apellidosp':'Apellidos',
            'fecha_nacimientop':'Fecha de nacimiento',
            'DPIP':'No. CUI',
            'direccionp':'Dirección domiciliar',
            'tel_casap':'Teléfono de casa',
            'tel_celp':'Teléfono Celular',
            'emailp':'Correo electrònico',
            'cantidad_convivientesp':'Cantidad de personas que viven en su casa',
            'conquien_vive':'Con quièn vive actualmente',
            'fotografiaP':'Fotografía',
            'municipio':'Municipio',
            'etnia':'Etnia',
            'genero':'Género',
            'razon':'Razón',
            'ingreso_total':'Ingreso Total',
            'total_gastos':'Total de Gastos',
            'edad':'Edad',
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
