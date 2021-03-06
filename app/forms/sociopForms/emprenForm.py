from django import forms
from app.models import Emprendimiento

class EmprenForm(forms.ModelForm):

    fecha_inicio = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        ), label="Fecha en la que inicia el emprendimiento"
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
                'muni':"Municipio en donde se ubica el emprendimiento",
                'estado_Emprendimiento':'Activo'}
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
                'class':'form-control',
                'required':False
            })
            if type(self.fields[field])==forms.BooleanField:
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input'
            })
        self.fields['muni'].empty_label = "Seleccione un municipio"
        self.fields['Tipoemp'].empty_label = "Seleccione tipo de emprendimiento"
