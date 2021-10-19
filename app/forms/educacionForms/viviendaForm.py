from django import forms
from app.models import vivienda

class VivForm(forms.ModelForm):
    class Meta:
        model = vivienda
        fields = ['cantidad_personas','cantidad_ambientes', 'energia_electrica', 'servicio_sanitario', 'letrina', 'techo','categoria', 'piso', 'muro', 'servicio']
        labels = {'cantidad_personas':"CantidadPersonas",
        'energia_electrica':'Energia electrica',
        'servicio_sanitario':'Sevicios sanitario',
        'letrina':'letrina',
        'techo':'Techo', 'piso':'piso',
        'muro':'muro',
        'servicio':'servicio', 'categoria':'categoria'}
        widgets = {
            'cantidad_personas': forms.TextInput(
                attrs={
                    'placeholder':'cantidad de personas',
                    'onblur':'agregar_forms_viviendas();'
                }
            )

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['techo'].empty_label = "Seleccione un techo"
            self.fields['piso'].empty_label = "Seleccione un Piso"
            self.fields['servicio'].empty_label = "Seleccione un servicio"
            self.fields['categoria'].empty_label = "Seleccione una categoria"
            self.fields['muro'].empty_label = "Seleccione tipo de muro"

class VivFormEdit(forms.ModelForm):
    class Meta:
        model = vivienda
        fields = ['cantidad_personas','cantidad_ambientes', 'energia_electrica', 'servicio_sanitario', 'letrina', 'techo','categoria', 'piso', 'muro', 'servicio', 'estado_vivienda']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['techo'].empty_label = "Seleccione un techo"
            self.fields['piso'].empty_label = "Seleccione un Piso"
            self.fields['servicio'].empty_label = "Seleccione un servicio"
            self.fields['categoria'].empty_label = "Seleccione una categoria"
            self.fields['muro'].empty_label = "Seleccione tipo de muro"