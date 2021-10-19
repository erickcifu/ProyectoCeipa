from django import forms
from app.models import religion

class ReligionForm(forms.ModelForm):
    class Meta:
        model = religion
        fields = ['nombre_religion','estado_religion']
        labels = {'nombre_religion':'Religion', 'estado_religion':'Estado'}
        widget = {'nombre_religion', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
