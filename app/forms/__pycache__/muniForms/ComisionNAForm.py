from django import forms
from app.models import ComisionNA

class Comision_NAForm(forms.ModelForm):
    estado_comision = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
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
        'cg_comision':'Cargo que ocupa en el grupo organizado',
        'inst_gobierno':'Gubernamental',
        'inst_publica':'Pública',
        'nombre_instit':'Nombre de la institución',
        'correo_instit':'Correo electrónico de la institución',
        'tel_instit':'No. Telefono de la institución',
        'institucion':'Nombre de la institución a la que pertenece',
        'participacion':'Participación dentro del grupo',
        'vacuna_comision':'Vacunado contra COVID-19',
        'estado_comision':'Activo/Inactivo',
        }
        widget = {'correo_personacna': forms.TextInput}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
