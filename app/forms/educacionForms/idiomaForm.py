from django import forms
from app.models import idioma

class IdiomaForm(forms.ModelForm):
    estado_idioma = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = idioma
        fields = ['nombre_idioma', 'descripcion_idioma', 'estado_idioma']
        labels = {'nombre_idioma':'Idioma', 'descripcion_idioma':'Descripcion_idioma', 'estado_idioma':'Estado'}
        widget = {'nombre_idioma', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
