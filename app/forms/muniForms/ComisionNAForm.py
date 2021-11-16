from django import forms
from app.models import ComisionNA

class Comision_NAForm(forms.ModelForm):
    estado_comision = forms.BooleanField()
    class Meta:
        model = ComisionNA
        fields = [
        'correo_personacna',
        'participacion_comina',
        'gorg_comision',
        'cg_comision',
        'inst_gobierno',
        'inst_publica',
        'nombre_instit',
        'correo_instit',
        'tel_instit',
        'vacuna_comision',
        'estado_comision']

        labels = {
        'correo_personacna':'Correo electrónico personal',
        'participacion_comina':'¿Participa en algún grupo organizado?',
        'gorg_comision':'Grupo organizado en el que participa',
        'cg_comision':'Cargo que ocupa',
        'inst_gobierno':'Gubernamental',
        'inst_publica':'Pública',
        'nombre_instit':'Nombre de la institución',
        'correo_instit':'Correo electrónico de la institución',
        'tel_instit':'No. Telefono de la institución',
        'institucion':'Nombre de la institución a la que pertenece',
        'vacuna_comision':'Vacunado contra COVID-19',
        'estado_comision':'Activo',
        }
        widget = {'correo_personacna': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'requiered':False
            })
            if field == 'estado_comision':
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
            if field == 'tel_instit':
                self.fields[field].widget.attrs.update({
                    'placeholder':'00000000',
                    'onblur':'isTelephoneNumber({});'.format('id_'+field),
            })
            if type(self.fields[field])==forms.EmailField:
                self.fields[field].widget.attrs.update({
                    'onblur':'isEmail({});'.format('id_'+field)
                })
            self.fields['gorg_comision'].empty_label = "Seleccione grupo organizado"
            self.fields['cg_comision'].empty_label = "Seleccione cargo en el grupo"
            self.fields['gorg_comision'].required = False
            self.fields['cg_comision'].required = False
