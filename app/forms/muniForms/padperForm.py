from django import forms
from app.models import PadPer

class PadPerForm(forms.ModelForm):
    class Meta:
        model = PadPer
        fields = ['medicamentos', 'persona', 'observacion', 'padecimiento', 'estado_padper']
        labels = {'medicamentos':'Medicamentos', 'persona':'persona', 'estado_padper':"Estado"}
        widget = {'nombre_comision': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['persona'].empty_label = "Seleccione a la Persona"
            self.fields['padecimiento'].empty_label = "Seleccione un padecimiento"
