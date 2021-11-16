from django import forms
from app.models import IdiomaPersona


class IdPerForm(forms.ModelForm):

    class Meta:
        model = IdiomaPersona
        fields = ['idioma', 'estado_ip']
        labels = {'idioma':"Idioma",
        'estado_ip':"Activo"}
        widget = {'idioma':forms.TextInput}


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['idioma'].empty_label = "Seleccione idioma"


            if type(self.fields[field])==forms.BooleanField:
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input'
                })
