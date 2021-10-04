from django import forms
from app.models import IdiomaPersona


class IdPerForm(forms.ModelForm):
    class Meta:
        model = IdiomaPersona
        fields = ['idioma', 'persona', 'estado_ip']
        labels = {'idioma':"idioma", 'persona':'Persona', 'estado_ip':"Estado"}
        widget = {'estado_ip': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['persona'].empty_label = "Seleccione persona"
            self.fields['idioma'].empty_label = "Seleccione idioma"
