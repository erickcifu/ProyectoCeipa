from django import forms
from app.models import Ausencia


class AusenciaForm(forms.ModelForm):
    class Meta:
        model = Ausencia
        fields = ['iniciof','finf','razon', 'estado_ausencia']
        labels = {'razon':"razon", 'estado_ausencia':"Estado"}
        widget = {'razon': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
