from django import forms
from app.models import Categoria


class CategoriaForm(forms.ModelForm):
    estado_categoria = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = Categoria
        fields = ['nombre_categoria', 'estado_categoria']
        labels = {'nombre_categoria':"categoria", 'estado_categoria':"Estado"}
        widget = {'nombre_categoria': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
