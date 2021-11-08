from django import forms
from app.models import departamento


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = departamento
        fields = ['nombre_departamento', 'estado_departamento']
        labels = {'nombre_departamento':"Departamento", 'estado_departamento':"Activo"}
        widget = {'nombre_departamento': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
