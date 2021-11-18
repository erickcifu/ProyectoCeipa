from django import forms
from app.models import AspectosSalud

class AspectosSaludForm(forms.ModelForm):
    estado_aspectosalud = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo"
    )
    class Meta:
        model = AspectosSalud
        fields = [
            'fractura',
            'descripcion_fractura',
            'operacion',
            'descripcion_operacion',
            'padecimiento',
            'descripcion_enfermedad',
            'recibe_tratamiento',
            'descripcion_tratamiento',
            'nombre_medicamento',
            'limitacion_fisica',
            'descripcion_limitacion',
            'estado_aspectosalud'
        ]

        labels = {
            'fractura':'Ha tenido alguna fractura',
            'descripcion_fractura':'Si ha tenido fracturas, escriba en que parte del cuerpo',
            'operacion':'Ha tenido alguna operacion',
            'descripcion_operacion':'Si ha tenido operaciones, describa en que parte del cuerpo',
            'padecimiento':'Tiene algúna enfermedad',
            'descripcion_enfermedad':'Si tiene alguna enfermedad, describa qué enfermedad es',
            'recibe_tratamiento':'Recibe algún tratamiento',
            'descripcion_tratamiento':'Si recibe algun tratamiento, describa que timpo de tratamiento es',
            'nombre_medicamento':'Nombre de Medicamento',
            'limitacion_fisica':'Cuenta con alguna limitación física',
            'descripcion_limitacion':'Si cuenta con alguna limitación física, describa que limitación fisica es',
            'estado_aspectosalud':'Activo'
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'required':False
            })
            if field == 'estado_aspectosalud':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input',
                'checked':True
            })
            required = self.fields[field].required
            if required:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
            })
            if type(self.fields[field])==forms.BooleanField:
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input'
            })
        self.fields['descripcion_fractura'].required = False
        self.fields['descripcion_operacion'].required = False
        self.fields['descripcion_enfermedad'].required = False
        self.fields['descripcion_tratamiento'].required = False
        self.fields['nombre_medicamento'].required = False
        self.fields['descripcion_limitacion'].required = False
