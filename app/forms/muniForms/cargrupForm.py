from django import forms
from app.models import CargoGrupo


class CarGForm(forms.ModelForm):
    class Meta:
        model = CargoGrupo
        fields = ['nombre_cg', 'estado_cg']
        labels = {'nombre_cg':"CargoGrupo", 'estado_cg':"Estado"}
        widget = {'nombre_cg': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
