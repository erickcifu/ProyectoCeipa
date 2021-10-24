from django import forms
from app.models import InfoEducacion

class InfoEducacionForm(forms.ModelForm):
    class Meta:
        model = InfoEducacion
        fields = ['nombre_establecimiento',
        'direccion_establecimiento',
        'jornada_estudio',
        #'grado_actual',
        'nombre_maestro',
        'tel_maestro',
        #'grupo_nin_adole',
        'nombre_grupo',
        'descripcion_grupo', 'recibido_formacion',
        'conocimiento_derechoshumanos', 'conocimiento_leyes', 'importancia_organizacion', 'te_motiva_participar', 'que_esperas_participar', 'estado_info_educacion']
        labels = {
            'nombre_establecimiento':'Nombre de Establecimiento',
            'direccion_establecimiento':'Direccion de Establecimiento',
            'jornada_estudio':'Jornada de Estudio',
            #'grado_actual':'Grado Actual',
            'nombre_maestro':'Nombre del Maestro',
            'tel_maestro':'Telefono del Maestro',
            #'grupo_nin_adole':'Participacion en un Grupo de niñez y adolecencia',
            'nombre_grupo':'Nombre del Grupo',
            'descripcion_grupo':'Descripción del Grupo',
            'recibido_formacion':'Por qué has recibido Formación de derechos humanos',
            'conocimiento_derechoshumanos':'Conocimiento a Derechos Humanos',
            'conocimiento_leyes':'Conocimiento a Leyes',
            'importancia_organizacion':'Importancia de Organización',
            'te_motiva_participar':'Motivación a Participar en consejo municipal',
            'que_esperas_participar':'Qué esperas al participar en el consejo Municipal de Niñez y Adolecencia',
            'estado_info_educacion':'Activo/Inactivo'}
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