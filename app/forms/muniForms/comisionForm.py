from django import forms
from app.models import Comision

class ComisionForm(forms.ModelForm):
    class Meta:
        model = Comision
        fields = ['nombre_comision', 'estado_comision']
        labels = {'nombre_comision':'Comision', 'estado_comision':"Estado"}
        widget = {'nombre_comision': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
