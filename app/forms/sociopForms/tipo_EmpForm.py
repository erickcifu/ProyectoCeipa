from django import forms
from app.models import TipoEmp

class TipoEmpForm(forms.ModelForm):
    class Meta:
        model = TipoEmp
        fields = ['emprendimiento_tipo', 'estado_tipoEmp']
        labels = {'emprendimiento_tipo':'Tipo de emprendimiento', 'estado_tipoEmp':'Activo/Inactivo'}
        widget = {
            'emprendimiento_tipo': forms.TextInput,
            'estado_tipoEmp': forms.CheckboxInput(
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
