from django import forms
from app.models import Cargo

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['nombre_cargo', 'estado_cargo']
        labels = {'nombre_cargo':'Cargo', 'estado_cargo':"Activo"}
        widget = {'nombre_cargo': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
