from django import forms
from app.models import Discapacidad

class DiscForm(forms.ModelForm):
    class Meta:
        model = Discapacidad
        fields = ['nombre_dis', 'estado_dis']
        labels = {'nombre_dis':'discapacidad', 'estado_dis':"Estado"}
        widget = {'nombre_dis': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
