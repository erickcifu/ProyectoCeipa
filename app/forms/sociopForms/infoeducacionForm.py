from django import forms
from app.models import InfoEducacion

class InfoEducacionForm(forms.ModelForm):
    class Meta:
        model = InfoEducacion
        fields = ['nombre_establecimiento',
        'direccion_establecimiento',
        'jornada_estudio',
        'grado_actual',
        'nombre_maestro',
        'tel_maestro',
        'participacion_grupo',
        'grupo_nin_adole',
        'recibido_formacion',
        'conocimiento_derechoshumanos', 'conocimiento_leyes', 'importancia_organizacion', 'te_motiva_participar',  'estado_info_educacion']
        labels = {
            'nombre_establecimiento':'Nombre de Establecimiento',
            'direccion_establecimiento':'Direccion de Establecimiento',
            'jornada_estudio':'Jornada de Estudio',
            'grado_actual':'Grado Actual',
            'nombre_maestro':'Nombre del Maestro',
            'tel_maestro':'Telefono del Maestro',
            'participacion_grupo':'¿Participa en algun grupo de niñez y adolescencia?',
            'grupo_nin_adole':'¿en que grupo de niñez y adolecencia?',
            'recibido_formacion':'¿Has recibido formación en derechos humanos de la niñez, adolecencia y juventud?',
            'conocimiento_derechoshumanos':'¿Qué sabes sobre derechos humanos de la niñez, adolescencia y juventud?',
            'conocimiento_leyes':'¿Conoces las leyes que protegen a la niñez y adolescencia?',
            'importancia_organizacion':'¿Crees que es importante que la niñez, adolescencia y juventud se organice y participe?',
            'te_motiva_participar':'¿Tienes motivación para participar en algún grupo de consejo municipal?',
            'estado_info_educacion':'Activo/Inactivo'
            }
        widget = {
            'nombre_establecimiento': forms.TextInput,
            'estado_info_educacion': forms.CheckboxInput(
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
