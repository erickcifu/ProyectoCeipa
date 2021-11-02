from django import forms
from app.models import MedioComuni, Persona

class MedioComuniForm(forms.ModelForm):
    estado = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = MedioComuni
        fields = ['nombre_medio',
        'correo',
        'vacuna_medio',
        'telefono',
        'cargo',
        't_medio',
        'estado']
        labels = {'nombre_medio':'Nombres de el medio',
        'correo':'Correo',
        'vacuna_medio':'Vacunado contra COVID-19',
        'telefono':"Telefono",  'cargo':'Cargo',
        't_medio':'Tipo de distribución del medio de comunicación',
        'estado':'Activo/Inactivo'}
        widget = {'nombre_medio', forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['cargo'].empty_label = "Seleccione Cargo"
