from django import forms

from app.models import Religion_alumno, religion, Alumno


class ReligionAlumnoForm(forms.ModelForm):
    estado_religionalumno = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs = { 'checked':True }
        ),
        required=False, label='Activo'
    )
    class Meta:
        model = Religion_alumno
        fields = ['religion', 'nombre_iglesia','direccion_iglesia', 'estado_religionalumno']
        labels = {'religion':'Religión','nombre_iglesia':"Nombre de Iglesia", 'direccion_iglesia':'Dirección de la iglesia','estado_religionalumno':"Activo"}
        widget = {'nombre_iglesia': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'required':False
            })
            if field == 'estado_religionalumno':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input',
                'checked':True
            })

            #Asignando nombres de funciones dependiendo el tipo de campo y si es requerido.
            required = self.fields[field].required
            if required:
                    self.fields[field].widget.attrs.update({
                        'onblur':'isRequeried({});'.format('id_'+field)
                    })

            self.fields['religion'].empty_label = "Seleccione Religion"
