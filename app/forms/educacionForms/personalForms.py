from django import forms
from app.models import personalEducativo

class PersonalForm(forms.ModelForm):
    class Meta:
        model = personalEducativo
        fields = ['nombres', 'apellidos', 'telefono_personal', 'email_personal', 'fechaNac_personal', 'direccion_personal', 'certificadoRenas_personal', 'estado_personal']
        labels = {'nombres':'Nombres', 'apellidos':'Apellidos', 'telefono_personal':'Telefono', 'email_personal':'Email', 'fechaNac_personal':'Fecha', 'direccion_personal':'Direccion', 'certificadoRenas_personal':'Certificado', 'estado_personal':'Estado'}
        widget = {'nombres', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
