from django import forms
from app.models import grados

class GradosForm(forms.ModelForm):
    class Meta:
        model = grados
        fields = ['nombre_grados','estado_grados']
        labels = {'nombre_grados':'Grados', 'estado_grados':'Estado'}
        widget = {'nombre_grados', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
