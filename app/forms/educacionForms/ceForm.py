from django import forms
from app.models import Ciclo_etapa
from app.models.educacion_model.ciclo import Ciclo

class CEForm(forms.ModelForm):
    class Meta:
        model = Ciclo_etapa
        fields = ['c_etapa','ciclo_c', 'estado_ce']
        labels = {'ciclo_c':'Ciclo',  'c_etapa':'Etapa', 'estado_ce':'Activo/Inactivo'}
        widget = {'estado_cg', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
                self.fields['c_etapa'].empty_label = "Seleccione la etapa"
                self.fields['ciclo_c'].empty_label = "Seleccione el ciclo"

class CEFormCreate(forms.ModelForm):
    class Meta:
        model = Ciclo_etapa
        fields = ['c_etapa', 'estado_ce']
        labels = {'ciclo_c':'Ciclo',  'c_etapa':'Etapa', 'estado_ce':'Activo/Inactivo'}
        widget = {'estado_ce', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
                self.fields['c_etapa'].empty_label = "Seleccione la etapa"
                self.fields['ciclo_c'].empty_label = "Seleccione el ciclo"
