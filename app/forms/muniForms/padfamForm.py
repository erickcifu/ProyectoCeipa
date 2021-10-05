from django import forms
from app.models import PadresFamilia

class PadFamForm(forms.ModelForm):
    class Meta:
        model = PadresFamilia
        fields = ['persona', 'grupo', 'cargo', 'programaC', 'estado_padres']
        labels = {'persona':'persona', 'grupo':'grupo', 'cargo':'cargo', 'programaC':'programaC','estado_padres':"Estado"}
        widget = {'persona': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['persona'].empty_label = "Seleccione a la Persona"
            self.fields['grupo'].empty_label = "Seleccione un grupo"
            self.fields['cargo'].empty_label = "Seleccione a la cargo"
            self.fields['programaC'].empty_label = "Seleccione un Programa Ceipa"
