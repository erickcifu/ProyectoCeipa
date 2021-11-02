from django import forms
from app.models import Ciclo_grado
from app.models.educacion_model.ciclo import Ciclo

class CGForm(forms.ModelForm):
    class Meta:
        model = Ciclo_grado
        fields = ['grado','ciclo','seccion', 'estado_cg']
        labels = {'ciclo':'Ciclo',  'grado':'Grado', 'seccion':'Sección', 'estado_cg':'Estado'}
        widget = {'estado_cg', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
                self.fields['grado'].empty_label = "Seleccione un Grado"
                self.fields['ciclo'].empty_label = "Seleccione un Ciclo"
                self.fields['seccion'].empty_label = "Seleccione una Seccion"

class CGFormCreate(forms.ModelForm):
    class Meta:
        model = Ciclo_grado
        fields = ['grado','seccion', 'estado_cg']
        labels = {'ciclo':'Ciclo',  'grado':'Grado', 'seccion':'Seccion', 'estado_cg':'Estado'}
        widget = {'estado_cg', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
                self.fields['grado'].empty_label = "Seleccione un Grado"
                self.fields['ciclo'].empty_label = "Seleccione un Ciclo"
                self.fields['seccion'].empty_label = "Seleccione una Seccion"

class CFCicloFormCreate(forms.Form):
    ciclo = forms.ModelChoiceField(queryset=Ciclo.objects.all())
