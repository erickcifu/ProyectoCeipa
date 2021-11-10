from django import forms
from app.models import GOrganizado

class GOrgForm(forms.ModelForm):
    estado_grupo = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = GOrganizado
        fields = ['nombre_grupo', 'estado_grupo']
        labels = {
        'nombre_grupo':'Nombre del grupo',
        'estado_grupo':'Activo/Inactivo',
        }
        widget = {'nombre_grupo': forms.TextInput}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
