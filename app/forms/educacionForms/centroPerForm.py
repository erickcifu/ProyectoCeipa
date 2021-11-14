from django import forms
from app.models import Centropersona
from app.models.educacion_model.personalEducativo import personalEducativo

class CentPerForm(forms.ModelForm):
    estado_centropersona = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = Centropersona
        fields = ['centro_Educativo','personal', 'estado_centropersona']
        labels = {'centro_Educativo':"centper", 'estado_centropersona':"Estado"}
        widget = {'centro_Educativo': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['centro_Educativo'].empty_label = "Seleccione un Centro Educativo"
            self.fields['personal'].empty_label = "Seleccione una persona"

class CentPerPorCentroEducativoForm(forms.ModelForm):
    class Meta:
        model = Centropersona
        fields = ['personal', 'estado_centropersona']
        labels = {'centro_Educativo':"centper", 'estado_centropersona':"Estado"}
        widget = {'centro_Educativo': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['personal'].empty_label = "Seleccione una persona"

class AsignarDirectorCentroEducativoForm(forms.ModelForm):
    class Meta:
        model = Centropersona
        fields = ['personal', 'estado_centropersona']
        labels = { 'estado_centropersona':"Estado"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['personal'].empty_label = "Seleccione una persona"
