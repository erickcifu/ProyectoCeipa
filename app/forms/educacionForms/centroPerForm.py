from django import forms
from app.models import Centropersona

class CentPerForm(forms.ModelForm):
    class Meta:
        model = Centropersona
        fields = ['centro_Educativo','personal', 'estado_centropersona']
        labels = {'centro_Educativo':"centper", 'estado_centropersona':"Estado"}
        widget = {'centro_Educativo': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
