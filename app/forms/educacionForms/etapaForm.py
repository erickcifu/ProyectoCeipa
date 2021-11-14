from django import forms
from app.models import Etapa

class EtapaForm(forms.ModelForm):
    class Meta:
        model = Etapa
        fields = ['nombre_etapa','estado_etapa']
        labels = {'nombre_etapa':'Nombre de la etapa',  'estado_etapa':'Activo/Inactivo'}
        widget = {'nombre_etapa', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
