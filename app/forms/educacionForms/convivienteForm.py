from django import forms
from app.models import Conviviente, Parentesco, vivienda

class ConvivienteForm(forms.ModelForm):

    parentesco = forms.ModelChoiceField(
        queryset = Parentesco.objects.filter(estado_parentesco=True)
        .order_by('nombre_parentesco')
    )
    fecha_nacimiento = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    estado_conviviente = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = Conviviente
        fields = ['nombres_conviviente', 'apellidos_conviviente', 'fecha_nacimiento', 'parentesco', 'estado_conviviente']
        labels = {'nombres_conviviente':'Nombres', 'apellidos_conviviente':'Apellidos', 'fecha_nacimiento':'Fecha de nacimiento', 'vivienda':'Vivienda', 'parentesco':'Parentesco', 'estado_conviviente':'Estado'}
        widget = {'nombres_conviviente', forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'requiered': False
            })
            if field == 'estado_conviviente':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input',
                'checked':True
            })
        self.fields['parentesco'].empty_label = "Seleccione Parentesco"

class ConvivienteFormEdit(forms.ModelForm):

    parentesco = forms.ModelChoiceField(
        queryset = Parentesco.objects.filter(estado_parentesco=True)
        .order_by('nombre_parentesco')
    )
    fecha_nacimiento = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    class Meta:
        model = Conviviente
        fields = ['nombres_conviviente', 'apellidos_conviviente', 'fecha_nacimiento', 'parentesco']
        labels = {'nombres_conviviente':'Nombres', 'apellidos_conviviente':'Apellidos', 'fecha_nacimiento':'Fecha de nacimiento', 'vivienda':'Vivienda', 'parentesco':'Parentesco', 'estado_conviviente':'Estado'}
        widget = {'nombres_conviviente', forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'requrided':False
            })

        self.fields['parentesco'].empty_label = "Seleccione Parentesco"
