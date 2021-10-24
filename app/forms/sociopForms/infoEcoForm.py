from django import forms
from app.models import InfoEconomica

class InfoecoForm(forms.ModelForm):
    class Meta:
        model = InfoEconomica
        fields = ['pariente','cantidad_mensual','procedencia_ingreso', 'observacion', 'estado_infoeco']
        labels = {
            'pariente':'Nombre del grado',
            'cantidad_mensual':'Cantidad de ingresos mensuales',
            'procedencia_ingreso':'Procedencia del ingreso',
            'observacion':'Observaciones',
            'estado_infoeco':'Activo/Inactivo'
        }
        widget = {
            'pariente': forms.TextInput,
            'estado_infoeco': forms.CheckboxInput(
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
            self.fields['cantidad_mensual'].required = False
            self.fields['procedencia_ingreso'].required = False
            self.fields['observacion'].required = False
