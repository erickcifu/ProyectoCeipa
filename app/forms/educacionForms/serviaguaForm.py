from django import forms
from app.models import Servicio_Agua


class ServiaguaForm(forms.ModelForm):
    class Meta:
        model = Servicio_Agua
        fields = ['servicio_agua', 'descripcion_servicio_agua', 'estado_agua']
        labels = {'servicio_agua':"Servicio de Agua", 'descripcion_servicio_agua':"Descripcion", 'estado_agua':"Estado"}
        widget = {'servicio_agua': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })