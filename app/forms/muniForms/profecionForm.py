from django import forms
from app.models import Profesion

class ProfesionForm(forms.ModelForm):
    class Meta:
        model = Profesion
        fields = ['nombre_profesion', 'estado_profesion']
        labels = {'nombre_profesion':'profesion', 'estado_profesion':"Activo"}
        widget = {'nombre_profesion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
