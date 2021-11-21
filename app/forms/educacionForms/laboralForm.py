from django import forms
from django.forms import widgets
#from django.forms.widgets import TimePickerInput
from app.models import AspectosLab

class LaboralForm(forms.ModelForm):
    estado_laborales = forms.BooleanField()
    hora_entrada = forms.TimeField(
        widget = forms.TextInput(
            attrs = { 'type': 'time' }
        )
    )
    hora_salida = forms.TimeField(
        widget = forms.TextInput(
            attrs = { 'type': 'time' }
        )
    )
    class Meta:
        model = AspectosLab
        fields = ['empleador',
        'tel_empleador',
        'area_trabaja',
        'jornada',
        'dias_trabajo',
        'hora_entrada',
        'hora_salida',
        'i_diario',
        'i_semanal',
        'i_quincenal',
        'i_mensual',
        'total_ingreso',
        'destino_ingreso',
        'edad_inicio_trabajo',
        'familia_migrante',
        'cantidad_familiares',
        'estado_laborales']
        labels = {
            'empleador':'¿Con quién trabaja?',
            'tel_empleador':'No. Telefono del empleador',
            'area_trabaja':'Especifique área en la que trabaja',
            'jornada':'Jornada Laboral',
            'dias_trabajo':'Días de trabajo',
            'hora_entrada':'Hora de entrada',
            'hora_salida':'Hora de salida',
            'i_diario':'Ingreso diario',
            'i_semanal':'Ingreso semanal',
            'i_quincenal':'Ingreso quincenal',
            'i_mensual':'Ingreso mensual',
            'total_ingreso':'Total de ingresos al mes',
            'destino_ingreso':'Destino de los ingresos',
            'edad_inicio_trabajo':'¿A qué edad empezó a trabajar?',
            'familia_migrante':'¿Tiene familia migrante?',
            'cantidad_familiares':'Si es así, ¿cuántos familiares tiene en el extranjero?',
            'estado_laborales':'Activo/Inactivo'
        }
        widget = {
            'empleador': forms.TextInput,
            #'hora_entrada': TimePickerInput(),
            #'hora_salida': TimePickerInput()
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control',
                    'required':False
                })
                if field == 'estado_laborales':
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
                if type(self.fields[field])==forms.EmailField:
                    self.fields[field].widget.attrs.update({
                        'onblur':'isEmail({});'.format('id_'+field)
                    })
            self.fields['ocup'].empty_label = "Seleccione ocupacion"
