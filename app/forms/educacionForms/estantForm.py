from django import forms
from app.models import EstudiosAnt

class EstAntForm(forms.ModelForm):
    estado_estudiosant = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = EstudiosAnt
        fields = ['grado','nombre_establecimiento', 'telefono_estudios_anteriores','repitente','apoyo_ong','nombre_ong','estado_estudiosant']
        labels = {'nombre_establecimiento':"Establecimiento anterior", 'repitente':"Repitente",'apoyo_ong':'Recibe apoyo de alguna ONG', 'nombre_ong':'Nombre de la ONG','telefono_estudios_anteriores':'Telefono de la organización','estado_estudiosant':"Estado"}
        widget = {'nombre_establecimiento': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

            if field == 'estado_estudiosant' or field == 'repitente':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input'
            })
            
            #Asignando nombres de funciones dependiendo el tipo de campo y si es requerido.
            required = self.fields[field].required
            if required:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
                })

            if field == 'telefono_estudios_anteriores':
                self.fields[field].widget.attrs.update({
                    'placeholder':'45002585',
                    'onblur':'isTelephoneNumber({});'.format('id_'+field),
                })

            self.fields['grado'].empty_label = "Seleccione un Grado"
            self.fields['telefono_estudios_anteriores'].empty_label = "00000000"
