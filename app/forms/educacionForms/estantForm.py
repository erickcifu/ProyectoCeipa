from django import forms
from app.models import EstudiosAnt

class EstAntForm(forms.ModelForm):
    class Meta:
        model = EstudiosAnt
        fields = ['grado','nombre_establecimiento', 'telefono','repitente','estado_estudiosant']
        labels = {'nombre_establecimiento':"estant", 'repitente':"Repitente",'estado_estudiosant':"Estado"}
        widget = {'nombre_establecimiento': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
