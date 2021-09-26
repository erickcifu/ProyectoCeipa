from django import forms
from app.models import Padecimiento


class PadeForm(forms.ModelForm):
    class Meta:
        model = Padecimiento
        fields = ['nombre_padecimiento', 'estado_padecimiento']
        labels = {'nombre_padecimiento':"Padecimiento", 'estado_padecimiento':"Estado"}
        widget = {'estado_padecimiento': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
