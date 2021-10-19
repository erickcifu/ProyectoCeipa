from django import forms
from app.models import ocupacion


class OcupaForm(forms.ModelForm):
    class Meta:
        model = ocupacion
        fields = ['nombre_ocupacion', 'estado_ocupacion']
        labels = {'nombre_ocupacion':"Ocupacion", 'estado_ocupacion':"Estado"}
        widget = {'estado_ocupacion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
