from django import forms
from app.models import LiderComunitario, Persona, CargoGrupo, GOrganizado, ProgramaC

class LiderComuniMuniForm(forms.ModelForm):
    persona = forms.ModelChoiceField(
        queryset = Persona.objects.filter(estado_persona=True)
        .order_by('persona')
    )
    cargo_grupo = forms.ModelChoiceField(
        queryset = CargoGrupo.objects.filter(estado_cg=True)
        .order_by('nombre_cg')
    )
    grupo_orga = forms.ModelChoiceField(
        queryset = GOrganizado.objects.filter(estado_grupo=True)
        .order_by('nombre_grupo')
    )
    programa_c = forms.ModelChoiceField(
        queryset = ProgramaC.objects.filter(estado_programa=True)
        .order_by('nombre_programa')
    )
    class Meta:
        model = LiderComunitario
        fields = ['persona', 'cargo_grupo', 'grupo_orga', 'programa_c', 'leer', 'escribir', 'vacuna_covid', 'periodo', 'fecha_inicio', 'fecha_fin', 'estado']
        labels = {'persona':'Persona', 'cargo_grupo':'Cargo en el grupo', 'grupo_orga':"Grupo Organizado", 'programa_c':'Programa en CEIPA', 'leer':'Sabe leer', 'escribir':"Sabe escribir", 'vacuna_covid':"Tiene la vacuna contra COVID", 'periodo':"Descripcion de su periodo", 'fecha_inicio':"Fecha de Inicio de periodo", 'fecha_fin':"Fecha de fin de periodo", 'estado':'Estado'}
        widget = {'persona', forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['persona'].empty_label = "Seleccione una Persona"
        self.fields['cargo_grupo'].empty_label = "Seleccione El cargo"
        self.fields['grupo_orga'].empty_label = "Seleccione Grupo"
        self.fields['programa_c'].empty_label = "Seleccione Programa en CEIPA"