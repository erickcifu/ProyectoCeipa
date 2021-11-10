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
            'nombre_establecimiento':'Nombre del establecimiento donde estudia actualmente',
            'direccion_establecimiento':'Direcciòn des establecimiento donde estudia actualmente',
            'jornada_estudio':'Jornada de estudios',
            'grado_actual':'Grado que cursa actualmente',
            'nombre_maestro':'Nombre del maestro(a) de grado',
            'tel_maestro':'No. Telèfono del maestro(a) de grado',
            'participacion_grupo':'¿Participa en algun grupo de niñez y adolescencia? (Cultural, deportivo, religioso)',
            'grupo_nin_adole':'¿En que grupo de niñez y adolecencia participa?',
            'recibido_formacion':'¿Ha recibido formación en derechos humanos de la niñez, adolecencia y juventud?',
            'conocimiento_derechoshumanos':'¿Qué sabe sobre derechos humanos de la niñez, adolescencia y juventud?',
            'conocimiento_leyes':'¿Conoce las leyes que protegen a la niñez y adolescencia?',
            'importancia_organizacion':'¿Cree que es importante que la niñez, adolescencia y juventud se organice y participe?',
            'te_motiva_participar':'¿Le motiva participar en el Concejo Municipal de Niñez y Adolescencia?',
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
