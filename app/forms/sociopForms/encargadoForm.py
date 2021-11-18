from django import forms
from app.models import Encargado

class EncargadoForm(forms.ModelForm):

    fecha_nacimientoE = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        ), label="Fecha de nacimiento"
    )
    estado_Encargado = forms.BooleanField(
        widget = forms.CheckboxInput(), label="Activo"
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
            'nombres_encar':"Nombre",
            'apellidos_encar':"Apellidos",
            'fecha_nacimientoE':"Fecha de nacimiento",
            'TelefonoE':"No. Teléfono",
            'parentesco':"Parentesco que tiene con el alumno",
            'octutor':'Ocupación',
            'estado_Encargado':'Activo'}
        widget = {
            'nombres_encar': forms.TextInput,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'required':False
            })
            if field == 'estado_Encargado':
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input',
                    'checked':True
            })
            if type(self.fields[field])==forms.BooleanField:
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input'
            })
            requiered = self.fields[field].required
            if requiered:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
            })
        self.fields['parentesco'].empty_label = "Seleccione el parentesco que tiene con el participante"
        self.fields['octutor'].empty_label = "Seleccione la ocupación del encargado"
