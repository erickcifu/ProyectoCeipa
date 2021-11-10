from django import forms

from app.models import municipio, departamento


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
