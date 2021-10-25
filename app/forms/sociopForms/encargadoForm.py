from django import forms
from app.models import Encargado

class EncargadoForm(forms.ModelForm):

    fecha_nacimientoE = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    estado_Encargado = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = Encargado
        fields = [
            'nombres_encar',
            'apellidos_encar',
            'fecha_nacimientoE',
            'TelefonoE',
            'parentesco',
            'octutor',
            'estado_Encargado'
            ]

        labels = {
            'nombres_encar':"Nombre del Ecargado",
            'apellidos_encar':"Apellidos del Encargado",
            'fecha_nacimientoE':"Fecha de nacimiento",
            'TelefonoE':"Telefono del Encargado",
            'parentesco':"Parentesco",
            'octutor':'Ocuypacion tutor',
            'estado_Encargado':'Activo/Inactivo'}
        widget = {
            'nombres_encar': forms.TextInput,
            'estado_Encargado': forms.CheckboxInput(
                attrs = {
                    'checked':True,
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['parentesco'].empty_label = "Seleccione un parentesco"
            self.fields['octutor'].empty_label = "Seleccione una Ocupacion"
