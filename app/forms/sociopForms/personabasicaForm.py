from django import forms
from django.forms import widgets
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
            'emailp':'Correo electrónico',
            'cantidad_convivientesp':'Cantidad de personas que viven en su casa',
            'conquien_vive':'Con quién vive actualmente',
            'fotografiaP':'Fotografía',
            'municipio':'Municipio',
            'etnia':'Etnia',
            'genero':'Género',
            'razon':'Razón por la que vive con esa/esas personas',
            'ingreso_total':'Total de ingresos',
            'total_gastos':'Total de gastos',
            'edad':'Edad',
            'estado_persona_basica':'Activo/Inactivo'}
        widget = {
            'nombres': forms.TextInput,
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'required': False
            })
            if field == 'estado_persona_basica':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input',
                'checked':True
            })
            required = self.fields[field].required
            if required:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
            })
            if field == 'tel_casap':
                self.fields[field].widget.attrs.update({
                    'placeholder':'00000000',
                    'onblur':'isTelephoneNumber({});'.format('id_'+field),
            })
            if field == 'tel_celp':
                self.fields[field].widget.attrs.update({
                    'placeholder':'00000000',
                    'onblur':'isTelephoneNumber({});'.format('id_'+field),
            })
            if type(self.fields[field])==forms.EmailField:
                self.fields[field].widget.attrs.update({
                    'onblur':'isEmail({});'.format('id_'+field)
            })
        self.fields['municipio'].empty_label = "Seleccione municipio"
        self.fields['etnia'].empty_label = "Seleccione grupo étnico"
        self.fields['genero'].empty_label = "Seleccione género"
