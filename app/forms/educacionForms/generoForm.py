from django import forms
from app.models import genero

class GeneroForm(forms.ModelForm):
    class Meta:
        model = genero
        fields = ['genero','estado_genero']
        labels = {'genero':'Genero', 'estado_genero':'Estado'}
        widget = {'genero', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
