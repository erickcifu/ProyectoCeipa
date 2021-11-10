from django import forms
from app.models import Area


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nombre_area', 'estado_area']
        labels = {'nombre_area':"Area", 'estado_area':"Estado"}
        widget = {'nombre_area': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
