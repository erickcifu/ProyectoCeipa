from django import forms
from app.models import AspectosLab

class LaboralForm(forms.ModelForm):
    estado_laborales = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={'checked':True}
        ), label="Activo/Inactivo"
    )
    hora_entrada = forms.TimeField()
    hora_salida = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'class':'time-pick'
            }
        )
    )
    class Meta:
        model = AspectosLab
        fields = ['empleador', 'tel_empleador', 'area_trabaja', 'jornada', 'dias_trabajo', 'hora_entrada','hora_salida', 'i_diario', 'i_semanal', 'i_quincenal', 'i_mensual', 'total_ingreso', 'destino_ingreso', 'edad_inicio_trabajo', 'estado_laborales']
        labels = {
            'empleador':'Con quien trabaja',
            'tel_empleador':'No. Telefono',
            'area_trabaja':'Especifique área',
            'jornada':'Jornada Laboral',
            'dias_trabajo':'Dias de trabajo',
            'hora_entrada':'Hora de entrada',
            'hora_salida':'Hora de salida',
            'i_diario':'Ingreso diario',
            'i_semanal':'Ingreso semanal',
            'i_quincenal':'Ingreso quicenal',
            'i_mensual':'Ingreso mensual',
            'total_ingreso':'Total de ingresos',
            'destino_ingreso':'Destino de los ingresos',
            'edad_inicio_trabajo':'Edad a la que empezó a trabajar',
            'estado_laborales':'Activo/Inactivo'
        }
        widget = {'empleador', forms.TextInput,
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
            self.fields['ocup'].empty_label = "Seleccione ocupacion"
