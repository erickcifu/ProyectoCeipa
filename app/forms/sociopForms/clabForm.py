from django import forms
from app.models import Caract_laborales

class ClabForm(forms.ModelForm):
    hora_entrada = forms.DateField(
        widget = forms.TextInput(
            attrs = { 'type': 'time' }
        ), required = False
    )
    hora_salida = forms.DateField(
        widget = forms.TextInput(
            attrs = { 'type': 'time' }
        ), required = False
    )
    class Meta:
        model = Caract_laborales
        fields = [
            'ha_trabajado',
            'razon_t',
            'edad_inicio',
            't_realizados',
            'trabaja_actualmente',
            'empleador_p',
            'hora_entrada',
            'hora_salida',
            'InfEconomica',
            'fam_extranjero',
            'op_extranjero',
            'op_empleos',
            'empleado',
            'propio',
            's_americano',
            'estado_claborales',

        ]
        labels = {
            'ha_trabajado':'Ha trabajado alguna vez',
            'razon_t':'Razón por la que trabajó',
            'edad_inicio':'A que edad empezó a trabajar',
            't_realizados':'Trabajos que ha realizado',
            'trabaja_actualmente':'Trabaja actualmente',
            'empleador_p':'Con quién trabaja',
            'hora_entrada':'Hora de entrada',
            'hora_salida':'Hora de salida',
            'InfEconomica':'Ingresos totales',
            'fam_extranjero':'Tiene familia en el extranjero',
            'op_extranjero':'Cree que para mejorar su vida es necesario salir del país',
            'op_empleos':'Cree que en su departamento/municipio se promueve la capacitación técnica, empleabilidad y generacién de Micro Empresas para jóvenes',
            's_americano':'Ha pensado en irse del país en busca del sueño americano',
            'estado_claborales':'Activo'
        }
        widget = {
            'estado_claborales': forms.CheckboxInput(
                attrs = {
                    'checked':True,
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'required':False
            })
            if field == 'estado_claborales':
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
