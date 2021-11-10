from django import forms
from app.models import IdiomaPersona


class IdPerForm(forms.ModelForm):
    estado_ip = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = IdiomaPersona
        fields = ['idioma', 'estado_ip']
        labels = {'idioma':"Idioma",
        'estado_ip':"Activo/Inactivo"}


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['idioma'].empty_label = "Seleccione idioma"
