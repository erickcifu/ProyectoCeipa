from django import forms
from app.models import FormacionLab

class LaboralSocioForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    fecha_fin_formacion = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    class Meta:
        model = FormacionLab
        fields = [
            'fecha_inicio',
            'fecha_fin_formacion',
            'horas_formacion',
        ]
        labels = {
            'fecha_inicio':'Fecha en la que inicia la formación laboral',
            'fecha_fin_formacion': 'Fecha de finalización de formación',
            'persona_formacion':'Participante',
            'horas_formacion':'Horas que durará la formación',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class LaboralEditForm(forms.ModelForm):
    class Meta:
        model = FormacionLab
        fields = [
            'fecha_inicio',
            'fecha_fin_formacion',
            'horas_formacion',
            'estado_formacion',
            'formacion_completada'
        ]
        labels = {
            'fecha_inicio':'Fecha en la que inicia la formación laboral',
            'fecha_fin_formacion': 'Fecha de finalización de formación',
            'horas_formacion':'Horas que durará la formación',
            'estado_formacion':'Activo/Inactivo',
            'formacion_completada':'Formación laboral completada',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
