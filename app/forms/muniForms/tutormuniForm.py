from django import forms
from app.models import TutorMuni

class TutorMuniForm(forms.ModelForm):
    fecha_nacimiento_T = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    estado_tutor = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = TutorMuni
        fields = ['nombres_tutor', 'apellidos_tutor',
        'parentesco','DPI_T',
        'fecha_nacimiento_T', 'direccion_tutor',
        'telefono_T', 'fotografia_tutor', 'estado_tutor']
        labels = {'nombres_tutor':'Nombres',
        'apellidos_tutor':'Apellidos',
        'parentesco':'Parentesco que tiene con el beneficiado',
        'DPI_T':"No. DPI",
        'fecha_nacimiento_T':'Fecha de nacimiento',
        'direccion_tutor':'Direccion',
        'telefono_T':"No. Telefono",
        'fotografia_tutor':"Fotografia",
        'estado_tutor':'Activo/Inactivo'}
        widget = {'nombres_tutor', forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['parentesco'].empty_label = "Seleccione su parentesco"
