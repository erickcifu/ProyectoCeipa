from django import forms
from app.models import Tipo_piso


class TpisoForm(forms.ModelForm):
    class Meta:
        model = Tipo_piso
        fields = ['tipo_piso', 'estado_tipopiso']
        labels = {'tipo_piso':"tpiso", 'estado_tipopiso':"Estado"}
        widget = {'tipo_piso': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
