from django import forms
from app.models import Caract_laborales

class ClabForm(forms.ModelForm):
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
            'fam_extranjero',
            'op_extranjero',
            'op_empleos',
            'empleado',
            'propio',
            's_americano',
            'InfEconomica',
            'estado_claborales',

        ]
        labels = {
            'ha_trabajado':'Ha trabajado alguna vez',
            'razon_t':'Razòn por la que trabajò',
            'edad_inicio':'A que edad empezò a trabajar',
            't_realizados':'Trabajos que ha realizado',
            'trabaja_actualmente':'Trabaja actualmente',
            'empleador_p':'Con quien trabaja',
            'hora_entrada':'Hora de entrada',
            'hora_salida':'Hora de salida',
            'fam_extranjero':'Tiene familia en el extranjero',
            'op_extranjero':'Cree que para mejorar su vida es necesario salir del paìs',
            'op_empleos':'Cree que en su departamento/municipio se promueve la capacitaciòn tècnica, empleabilidad y generaciòn de Micro Empresas para jòvenes',
            's_americano':'Ha pensado en irse del paìs en busca del sueño americano',
            'estado_claborales':'Activo/Inactivo'
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
                'class':'form-control'
            })
