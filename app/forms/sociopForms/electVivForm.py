from django import forms
from app.models import ElectVivienda

class ElectvivForm(forms.ModelForm):
    class Meta:
        model = ElectVivienda
        fields = ['elect']
        labels = {'elect':'Electrodomestico',}
        widget = {
            'elect': forms.TextInput,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['elect'].empty_label = 'Seleccione electrodomestico'
