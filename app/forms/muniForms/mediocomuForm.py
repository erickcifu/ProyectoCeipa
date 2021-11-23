from django import forms
from app.models import MedioComuni, Persona

class MedioComuniForm(forms.ModelForm):
    class Meta:
        model = MedioComuni
        fields = ['nombre_medio',
        'correo_medio',
        'vacuna_medio',
        'telefono_medio',
        'cargo',
        't_medio',
        'estado']
        labels = {'nombre_medio':'Nombres de el medio',
        'correo_medio':'Correo',
        'vacuna_medio':'Vacunado contra COVID-19',
        'telefono_medio':"Telefono",  'cargo':'Cargo que ocupa el representante',
        't_medio':'Tipo de distribución del medio de comunicación',
        'estado':'Activo'}
        widget = {'nombre_medio', forms.TextInput}

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
            requiered = self.fields[field].required
            if requiered:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
            })
            if type(self.fields[field])==forms.EmailField:
                self.fields[field].widget.attrs.update({
                    'onblur':'isEmail({});'.format('id_'+field)
                })
        self.fields['cargo'].empty_label = "Seleccione Cargo"
