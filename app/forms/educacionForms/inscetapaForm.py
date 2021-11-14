from django import forms
from app.models import Inscripcion_etapa, Ciclo, Etapa
from app.models.educacion_model.centro_educativo import centro_educativo

class InscEtapaForm(forms.ModelForm):
    class Meta:
        model = Inscripcion_etapa
        fields = [
            'centro_educ_etapa',
            'alumno_etapa',
            'ciclo_etapa',
            'etapa_promovido',
            'etapa_retirado',
            'insc_etapa_estado',
        ]
        labels = {
            'centro_educ_etapa':'Centro educativo',
            'alumno_etapa':'Alumno',
            'ciclo_etapa':'Ciclo escolar',
            'etapa_promovido':'Promovido',
            'etapa_retirado':'Retirado',
            'insc_etapa_estado':'Activo/Inactivo',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['centro_educ_etapa'].empty_label = "Seleccione un centro educativo"
            self.fields['alumno_etapa'].empty_label = "Seleccione un alumno"
            self.fields['ciclo_etapa'].empty_label = "Seleccione un ciclo etapa"
