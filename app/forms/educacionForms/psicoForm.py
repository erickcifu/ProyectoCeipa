from django import forms
from app.models import psicologico


class PsicoForm(forms.ModelForm):
    fecha_Analisis = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    estado_psicologico = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = psicologico
        fields = ['Analisis_psicologico', 'fecha_Analisis','tratamiento', 'Entrevistador','estado_psicologico']
        labels = {'Analisis_psicologico':"Psicologico",'fecha_Analisis':'Fecha Analisis', 'tratamiento':'tratamiento','Entrevistador':'Entrevistador','estado_psicologico':"Estado"}
        widget = {'Analisis_psicologico': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            #agreango el nombre de la funcion para utilizarla en la plantilla
            required = self.fields[field].required
            if required:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
                })

            if type(self.fields[field])==forms.BooleanField:
                self.fields[field].widget.attrs.update({
                'class':'form-check-input'
            })
