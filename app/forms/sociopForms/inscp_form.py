from django import forms
from app.models import Taller, PersonaBasica, Inscripcionp
from app.models.educacion_model.municipioModel import municipio

class EmprenForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    estado_Emprendimiento = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = Emprendimiento
        fields = [
            'nombres_emp',
            'Monto_Capital',
            'fecha_inicio',
            'Tipoemp',
            'muni',
            'estado_Emprendimiento'
            ]

        labels = {
                'nombres_emp':"Nombre del emprendimiento:",
                'Monto_Capital':"Monto del capital en Q",
                'fecha_inicio':"Fecha de inicio del emprendimiento",
                'Tipoemp':"Tipo de emprendimiento",
                'muni':"Municipio",
                'estado_Emprendimiento':'Activo/Inactivo'}
        widget = {
            'nombres_emp': forms.TextInput,
            'estado_Emprendimiento': forms.CheckboxInput(
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
            self.fields['muni'].empty_label = "Seleccione un municipio"
            self.fields['Tipoemp'].empty_label = "Seleccione tipo de emprendimiento"
