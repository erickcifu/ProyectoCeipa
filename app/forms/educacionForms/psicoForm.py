from django import forms
from app.models import psicologico


class PsicoForm(forms.ModelForm):
    fecha_Analisis = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    estado_psicologico = forms.BooleanField()
    class Meta:
        model = psicologico
        fields = ['Analisis_psicologico',
        'fecha_Analisis',
        'tratamiento',
        'tiene_sueños',
        'sueños',
        'Entrevistador',
        'estado_psicologico']
        labels = {'Analisis_psicologico':"Análisis psicológico",
        'fecha_Analisis':'Fecha en la que se realizó el análisis',
        'tratamiento':'Descripción del tratamiento que recibe',
        'tiene_sueños':'Tiene sueños',
        'sueños':'¿Cuáles son sus sueños?',
        'Entrevistador':'Entrevistador',
        'estado_psicologico':"Activo"}
        widget = {'Analisis_psicologico': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            if field == 'estado_psicologico':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input',
                'checked':True
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
