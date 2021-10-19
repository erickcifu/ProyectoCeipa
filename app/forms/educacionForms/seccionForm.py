from django import forms
from app.models import seccion


class SeccionForm(forms.ModelForm):
    class Meta:
        model = seccion
        fields = ['nombre_seccion', 'estado_seccion']
        labels = {'nombre_seccion':"Seccion", 'estado_seccion':"Estado"}
        widget = {'nombre_seccion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
