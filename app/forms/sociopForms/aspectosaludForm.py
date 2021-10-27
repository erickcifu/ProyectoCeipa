from django import forms
from app.models import AspectosSalud

class AspectosSaludForm(forms.ModelForm):
    estado_aspectosalud = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
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
            'descripcion_fractura':'Descripción de Fractura',
            'operacion':'Ha tenido alguna operacion',
            'descripcion_operacion':'Descripción Operación',
            'padecimiento':'Tienen algún padecimiento',
            'descripcion_enfermedad':'Descripción de Enfermedad',
            'recibe_tratamiento':'Recibe algún tratamiento',
            'descripcion_tratamiento':'Descripción del tratamiento',
            'nombre_medicamento':'Nombre de Medicamento',
            'limitacion_fisica':'Cuenta con alguna limitación física',
            'descripcion_limitacion':'Descripción de Limitaciones',
            'estado_aspectosalud':'Activo/Inactivo'
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['descripcion_fractura'].required = False
            self.fields['descripcion_operacion'].required = False
            self.fields['descripcion_enfermedad'].required = False
            self.fields['descripcion_tratamiento'].required = False
            self.fields['nombre_medicamento'].required = False
            self.fields['descripcion_limitacion'].required = False
