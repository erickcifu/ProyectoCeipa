from django import forms
from app.models import Parentesco

class ParentescoForm(forms.ModelForm):
    class Meta:
        model = Parentesco
        fields = ['nombre_parentesco', 'descripcion_parentesco', 'estado_parentesco']
        labels = {'nombre_parentesco':"Tipo de parentesco", 'descripcion_parentesco':"Descripcion del Parentesco", 'estado_parentesco':"Estado"}
        widget = {'descripcion_parentesco': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
