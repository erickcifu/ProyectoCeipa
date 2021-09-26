from django import forms
from app.models import Ciclo

class CicloForm(forms.ModelForm):
    class Meta:
        model = Ciclo
        fields = ['anio', 'estado_ciclo']
        labels = {'anio':'Ciclo', 'estado_ciclo':"Estado"}
        widget = {'anio', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
