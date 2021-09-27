from django import forms
from app.models import Conviviente, Parentesco, vivienda

class ConvivienteForm(forms.ModelForm):
    vivienda = forms.ModelChoiceField(
        queryset = vivienda.objects.filter(estado_vivienda=True)
        .order_by('cantidad_ambientes')
    )
    parentesco = forms.ModelChoiceField(
        queryset = Parentesco.objects.filter(estado_parentesco=True)
        .order_by('nombre_parentesco')
    )
    class Meta:
        model = Conviviente
        fields = ['nombres_conviviente', 'apellidos_conviviente', 'fecha_nacimiento', 'vivienda', 'parentesco', 'estado_conviviente']
        labels = {'nombres_conviviente':'Nombres', 'apellidos_conviviente':'Apellidos', 'fecha_nacimiento':'Fecha de nacimiento', 'vivienda':'Vivienda', 'parentesco':'Parentesco', 'estado_conviviente':'Estado'}
        widget = {'nombres_conviviente', forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['vivienda'].empty_label = "Seleccione ambiente de vivienda"
        self.fields['parentesco'].empty_label = "Seleccione Parentesco"