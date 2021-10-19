from django import forms
from app.models import Grado


class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ['nombre_grado', 'descripcion_grado', 'estado_grado']
        labels = {'nombre_grado':"Grado", 'descripcion_grado':"Descripcion", 'estado_grado':"Estado"}
        widget = {'nombre_grado': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
