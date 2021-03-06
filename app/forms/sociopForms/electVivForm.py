from django import forms
from app.models import ElectVivienda, Electrodomesticos

class ElectvivForm(forms.ModelForm):
    class Meta:
        model = ElectVivienda
        fields = ['elect',]
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
            
            if type(self.fields[field])==forms.BooleanField:
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input'
            })
        self.fields['elect'].empty_label = 'Seleccione electrodomestico'
