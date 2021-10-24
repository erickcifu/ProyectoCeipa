from django import forms
from app.models import AspectosSalud

class AspectosSaludForm(forms.ModelForm):
    class Meta:
        model = AspectosSalud
        fields = ['fractura','descripcion_fractura', 'operacion', 'descripcion_operacion', 'padecimiento', 'descripcion_enfermedad', 'recibe_tratamiento', 'descripcion_tratamiento', 'nombre_medicamento', 'limitacion_fisica', 'descripcion_limitacion', 'estado_aspectosalud']
        labels = {
            'fractura':'Fractura',
            'descripcion_fractura':'Descripción de Fractura',
            'operacion':'Operacion',
            'descripcion_operacion':'Descripción Operación',
            'padecimiento':'Padecimiento',
            'descripcion_enfermedad':'Descripción de Enfermedad',
            'recibe_tratamiento':'Tratamiento que recibe',
            'descripcion_tratamiento':'Descripción de Tratamiento',
            'nombre_medicamento':'Nombre de Medicamento',
            'limitacion_fisica':'Limitación Física',
            'descripcion_limitacion':'Descripción de Limitaciónes',
            'estado_aspectosalud':'Activo/Inactivo'}
        widget = {
            'fractura': forms.TextInput,
            'estado_aspectosalud': forms.CheckboxInput(
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