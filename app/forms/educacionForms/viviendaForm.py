from django import forms
from app.models import vivienda

class VivForm(forms.ModelForm):
    class Meta:
        model = vivienda
        fields = ['cantidad_personas','cantidad_ambientes', 'techo','piso','servicio','estudiante','estado_vivienda']
        labels = {'cantidad_personas':"CantidadPersonas",'techo':'Techo', 'piso':'piso','servicio':'servicio','estado_vivienda':"Estado"}
        widget = {'cantidad_personas': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['techo'].empty_label = "Seleccione un techo"
            self.fields['piso'].empty_label = "Seleccione un Piso"
            self.fields['servicio'].empty_label = "Seleccione un servicio"
            self.fields['estudiante'].empty_label = "Seleccione un Alumno"
