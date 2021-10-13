from django import forms
from app.models import Apadecimiento


class APadeForm(forms.ModelForm):
    class Meta:
        model = Apadecimiento
        fields = ['padecimiento','tratamiento', 'estado_Alpadecimiento']
        labels = {'padecimiento':"AlumPad", 'estado_Alpadecimiento':"Estado"}
        widget = {'estado_Alpadecimiento': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['padecimiento'].empty_label = "Seleccione un padecimiento"
