from django import forms
from app.models import LiderComunitario, Persona, CargoGrupo, GOrganizado, ProgramaC

class LiderComuniMuniForm(forms.ModelForm):
    cargo_grupo = forms.ModelChoiceField(
        queryset = CargoGrupo.objects.filter(estado_cg=True)
        .order_by('nombre_cg'), label ="Cargo que ocupa en el grupo"
    )
    grupo_orga = forms.ModelChoiceField(
        queryset = GOrganizado.objects.filter(estado_grupo=True)
        .order_by('nombre_grupo'), label ="Grupo al que pertenece"
    )
    programa_c = forms.ModelChoiceField(
        queryset = ProgramaC.objects.filter(estado_programa=True)
        .order_by('nombre_programa'), label ="Programa al que pertenece dentro de CEIPA", required="False"
    )
    estado = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    fecha_inicio = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    fecha_fin = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    class Meta:
        model = LiderComunitario
        fields = ['cargo_grupo', 'grupo_orga', 'programa_c', 'leer', 'escribir', 'vacuna_covid', 'periodo', 'fecha_inicio', 'fecha_fin', 'correo_lideres','estado']
        labels = {'cargo_grupo':'Cargo que tendrà en el grupo', 'grupo_orga':"Grupo organizado al que pertenece", 'programa_c':'Programa al que pertenece en CEIPA', 'leer':'Sabe leer', 'escribir':"Sabe escribir", 'vacuna_covid':"Tiene la vacuna contra COVID", 'periodo':"Tiempo que durarà el cargo", 'fecha_inicio':"Fecha de Inicio de periodo", 'fecha_fin':"Fecha de fin de periodo", 'correo_lideres':'Correo electrónico' ,'estado':'Activo/Inactivo'}


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['cargo_grupo'].empty_label = "Seleccione El cargo"
        self.fields['grupo_orga'].empty_label = "Seleccione Grupo"
        self.fields['programa_c'].empty_label = "Seleccione Programa en CEIPA"
