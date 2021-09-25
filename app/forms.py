from django import forms

from .models.educacion_model.parentesco import Parentesco
from .models.educacion_model.departamento import departamento
from .models.educacion_model.municipioModel import municipio

class ParentescoForm(forms.ModelForm):
    class Meta:
        model = Parentesco
        fields = ['nombre_parentesco', 'descripcion_parentesco', 'estado_parentesco']
        labels = {'nombre_parentesco':"Tipo de parentesco", 'descripcion_parentesco':"Descripcion del Parentesco", 'estado_parentesco':"Estado"}
        widget = {'descripcion_parentesco': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = departamento
        fields = ['nombre_departamento', 'estado_departamento']
        labels = {'nombre_departamento':"Departamento", 'estado_departamento':"Estado"}
        widget = {'nombre_departamento': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class MunicipioForm(forms.ModelForm):
    dep = forms.ModelChoiceField(
        queryset = departamento.objects.filter(estado_departamento=True)
        .order_by('nombre_departamento')
    )
    class Meta:
        model = municipio
        fields = ['dep', 'nombre_municipio', 'estado_municipio']
        labels = {'nombre_municipio':"Municipio", 'estado_municipio':"Estado"}
        widget = {'nombre_municipio': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['dep'].empty_label = "Seleccione Departamento"