from django import forms
from app.models import centro_educativo


class CentEduForm(forms.ModelForm):
    class Meta:
        model = centro_educativo
        fields = ['nombre_centro', 'direccion_centro', 'codigo_centro', 'estado_centro']
        labels = {'nombre_centro':"CentroEducativo", 'direccion_centro':'Direccion', 'codigo_centro':'Codigo', 'estado_centro':"Estado"}
        widget = {'nombre_centro': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
