from django import forms
from app.models import TutorMuni

class TutorMuniForm(forms.ModelForm):
    class Meta:
        model = TutorMuni
        fields = ['nombres_tutor', 'apellidos_tutor', 'DPI', 'fecha_nacimiento', 'direccion_tutor', 'telefono', 'fotografia', 'estado_tutor']
        labels = {'nombres_tutor':'Nombres', 'apellidos_tutor':'Apellidos', 'DPI':"DPI", 'fecha_nacimiento':'Fecha de nacimiento', 'direccion_tutor':'Direccion', 'telefono':"Telefono", 'correo':"Correo", 'fotografia':"Fotografia", 'estado_tutor':'Estado'}
        widget = {'nombres_tutor', forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })