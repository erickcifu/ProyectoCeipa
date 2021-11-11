from django import forms
from app.models import PartidoPolitic


class PartidoPoliticForm(forms.ModelForm):
    class Meta:
        model = PartidoPolitic
        fields = ['nombre_partido', 'estado']
        labels = {'nombre_partido':"Nombre Partido Politico", 'estado':"Estado"}
        widget = {'nombre_partido': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })