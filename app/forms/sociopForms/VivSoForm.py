from django import forms
from app.models import ViviendaSocio

class ViviendaSForm(forms.ModelForm):
    estado_vivsocio = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
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
            'numero_habitantes':'numero habitantes',
            'otra_Viv':'Tiene otra vivienda',
            'desc_Otra_Viv':'Descrpcion de la otra Vivienda',
            'Telefono':'Telefono de la vivienda',
            'tipopiso':'Tipo de piso',
            'tipotecho':'tipo de techo',
            'tipomuro':'Tipo de muro',
            'tipovivienda':'tipo de vivienda',
            'agua_potable':'agua potable',
            'energia_elect':'energia electrica',
            'dreaje':'dreaje',
            'nivel_Eco_Alto':'nivel economico Alto',
            'nivel_Eco_medio':'nivel Economico medio',
            'nivel_Eco_bajo':'nivel Economico bajo',
            'pobre':'pobre',
            'no_pobre':'no pobre',
            'Extemadamente_pobre':'Extemadamente pobre',
            'estado_vivsocio':'Activo/Inactivo'}
        widget = { 'numero_habitantes': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['tipotecho'].empty_label = "Seleccione un techo"
            self.fields['tipopiso'].empty_label = "Seleccione un Piso"
            self.fields['tipomuro'].empty_label = "Seleccione un muro"
            self.fields['tipovivienda'].empty_label = "Seleccione una tipo de vivienda"
            self.fields['numero_habitantes'].required = False
