from django import forms
from app.models import etnia


class EtniaForm(forms.ModelForm):
    class Meta:
        model = etnia
        fields = ['nombre_etnia', 'descripcion_etnia', 'estado_etnia']
        labels = {'nombre_etnia':"Nombre de Etnia", 'descripcion_etnia':"Descripcion", 'estado_etnia':"Estado"}
        widget = {'nombre_etnia': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })