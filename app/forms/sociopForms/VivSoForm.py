from django import forms
from app.models import ViviendaSocio

class ViviendaSForm(forms.ModelForm):
    estado_vivsocio = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo"
    )
    class Meta:
        model = ViviendaSocio
        fields = [
            'numero_habitantes',
            'otra_Viv',
            'desc_Otra_Viv',
            'Telefono',
            'tipopiso',
            'tipotecho',
            'tipomuro',
            'tipovivienda',
            'agua_potable',
            'energia_elect',
            'dreaje',
            'nivel_Eco_Alto',
            'nivel_Eco_medio',
            'nivel_Eco_bajo',
            'pobre',
            'no_pobre',
            'Extemadamente_pobre',
            'estado_vivsocio'
            ]

        labels = {
            'numero_habitantes':'Cantidad de habitaciones en la vivienda',
            'otra_Viv':'Sus padres tienen otra vivienda',
            'desc_Otra_Viv':'Si los padres tienen otra vivienda, agregar una descripción',
            'Telefono':'Teléfono',
            'tipopiso':'Tipo de piso',
            'tipotecho':'Tipo de techo',
            'tipomuro':'Tipo de pared',
            'tipovivienda':'La vivienda en la que habita es',
            'agua_potable':'Agua potable',
            'energia_elect':'Energía eléctrica',
            'dreaje':'Drenaje',
            'nivel_Eco_Alto':'Alto',
            'nivel_Eco_medio':'Medio',
            'nivel_Eco_bajo':'Bajo',
            'pobre':'Pobre',
            'no_pobre':'No pobre',
            'Extemadamente_pobre':'Extremadamente pobre',
            'estado_vivsocio':'Activo'}
        widget = { 'numero_habitantes': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'required':False
            })
            if field == 'estado_vivsocio':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input',
                'checked':True
            })
            required = self.fields[field].required
            if required:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
            })
            if type(self.fields[field])==forms.BooleanField:
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input'
            })
        self.fields['tipotecho'].empty_label = "Seleccione tipo de techo"
        self.fields['tipopiso'].empty_label = "Seleccione tipo de piso"
        self.fields['tipomuro'].empty_label = "Seleccione tipo de pared"
        self.fields['tipovivienda'].empty_label = "Seleccione categoría de la vivienda"
