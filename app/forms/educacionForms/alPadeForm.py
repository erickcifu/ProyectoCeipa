from django import forms
from app.models import Apadecimiento,Padecimiento


class APadeForm(forms.ModelForm):
    #padecimiento = forms.ModelMultipleChoiceField(queryset=Padecimiento.objects.all())
    estado_Alpadecimiento = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = Apadecimiento
        fields = ['padecimiento','tratamiento', 'estado_Alpadecimiento']
        labels = {'padecimiento':"AlumPad", 'tratamiento':'Tratamiento','estado_Alpadecimiento':"Estado"}
        widget = {'estado_Alpadecimiento': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['padecimiento'].empty_label = "Seleccione un padecimiento"
