from django import forms
from app.models import Tipo_muro


class ParedForm(forms.ModelForm):
    class Meta:
        model = Tipo_muro
        fields = ['tipo_muro', 'descripcion_muro', 'estado_muro']
        labels = {'tipo_muro':"Tipo de Pared o Muro", 'descripcion_muro':"Descripcion", 'estado_muro':"Estado"}
        widget = {'tipo_muro': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })