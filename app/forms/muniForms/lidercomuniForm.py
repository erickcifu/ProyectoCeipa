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
    fecha_inicio_l = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        ), label="Fecha de inicio del periodo"
    )
    fecha_fin_l = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        ), label="Fecha de finalización del periodo"
    )
    estado_liders = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo"
    )
    class Meta:
        model = LiderComunitario
        fields = ['cargo_grupo',
        'grupo_orga', 'programa_c',
         'leer_l', 'escribir_l',
          'vacuna_covid_l', 'periodo',
          'fecha_inicio_l', 'fecha_fin_l',
          'correo_lideres','estado_liders']
        labels = {'cargo_grupo':'Cargo que tendrá en el grupo',
        'grupo_orga':"Grupo organizado al que pertenece",
        'programa_c':'Programa al que pertenece en CEIPA',
        'leer_l':'Sabe leer', 'escribir_l':"Sabe escribir",
        'vacuna_covid_l':"Tiene la vacuna contra COVID",
        'periodo':"Tiempo que durará el cargo",
        'fecha_inicio_l':"Fecha de Inicio de periodo",
        'fecha_fin_l':"Fecha de fin de periodo",
        'correo_lideres':'Correo electrónico' ,'estado_liders':'Activo'}


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'required': False
            })

            if type(self.fields[field])==forms.BooleanField:
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input'
            })
            requiered = self.fields[field].required
            if requiered:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
            })
            if type(self.fields[field])==forms.EmailField:
                self.fields[field].widget.attrs.update({
                    'onblur':'isEmail({});'.format('id_'+field)
                })
        self.fields['cargo_grupo'].empty_label = "Seleccione El cargo"
        self.fields['grupo_orga'].empty_label = "Seleccione Grupo"
        self.fields['programa_c'].empty_label = "Seleccione Programa en CEIPA"
