from django import forms
from app.models import vivienda

class VivForm(forms.ModelForm):
    class Meta:
        model = vivienda
        fields = ['cantidad_personas','cantidad_ambientes', 'energia_electrica', 'servicio_sanitario', 'letrina', 'techo','categoria', 'piso', 'muro','servicio_internet', 'servicio', 'estado_vivienda']
        labels = {'cantidad_personas':"CantidadPersonas",
        'cantidad_ambientes':'Cantidad de ambientes',
        'energia_electrica':'Energia electrica',
        'servicio_sanitario':'Sevicios sanitario',
        'letrina':'letrina',
        'techo':'Techo', 'piso':'piso',
        'servicio_internet':'Servicio de internet',
        'muro':'muro',
        'servicio':'servicio', 'categoria':'categoria',
        'estado_vivienda':'Activo'}
        # widgets = {
        #     'cantidad_personas': forms.TextInput(
        #         attrs={
        #             'placeholder':'cantidad de personas',
        #             'onblur':'agregar_forms_viviendas();',
        #             'min':1,
        #             'max':2,
        #         }
        #     )
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            if field == 'estado_vivienda':
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
            if field == 'cantidad_personas':
                self.fields[field].widget.attrs.update({
                    'placeholder':'cantidad de personas',
                    'onblur':'agregar_forms_viviendas();',
                    'min':1,
                    'max':2,
                })
            if type(self.fields[field])==forms.BooleanField:
                self.fields[field].widget.attrs.update({
                'class':'form-check-input'
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
