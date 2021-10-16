from django import forms
from app.models import Tipo_techo


class TechoForm(forms.ModelForm):
    class Meta:
        model = Tipo_techo
        fields = ['tipo_techo', 'descripcion_techo', 'estado_techo']
        labels = {'tipo_techo':"Tipo de techo", 'descripcion_techo':"Descripcion", 'estado_techo':"Estado"}
        widget = {'tipo_techo': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })