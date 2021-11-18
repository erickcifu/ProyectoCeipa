from django import forms
from app.models import InfoEconomica

class InfoecoForm(forms.ModelForm):
    class Meta:
        model = InfoEconomica
        fields = ['pariente',
        'cantidad_mensual',
        'procedencia_ingreso',
        'observacion',
        'estado_infoeco']
        labels = {
            'pariente':'Nombre del pariente',
            'cantidad_mensual':'Cantidad de ingresos mensuales',
            'procedencia_ingreso':'Procedencia del ingreso',
            'observacion':'Observaciones',
            'estado_infoeco':'Activo'
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
                'class':'form-control',
                'required':False
            })
            if field == 'estado_infoeco':
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
