from django import forms
from app.models import Tutor, municipio, genero, Parentesco

class TutorForm(forms.ModelForm):
    genero = forms.ModelChoiceField(
        queryset = genero.objects.filter(estado_genero=True)
        .order_by('genero')
    )
    parentesco = forms.ModelChoiceField(
        queryset = Parentesco.objects.filter(estado_parentesco=True)
        .order_by('nombre_parentesco')
    )
    fecha_nacimiento_tutor = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    estado_tutor = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = Tutor
        fields = ['nombres_tutor', 'apellidos_tutor', 'DPI_tutor', 'fecha_nacimiento_tutor', 'direccion_tutor', 'telefono_tutor', 'correo_tutor', 'fotografia_t', 'muni', 'genero', 'parentesco', 'estado_tutor']
        labels = {'nombres_tutor':'Nombres', 'apellidos_tutor':'Apellidos', 'DPI_tutor':"DPI", 'fecha_nacimiento_tutor':'Fecha de nacimiento', 'direccion_tutor':'Direccion', 'telefono_tutor':"Telefono", 'correo_tutor':"Correo", 'fotografia_t':"Fotografia", 'muni':"Municipio", 'genero':"Genero", 'parentesco':'Parentesco', 'estado_tutor':'Estado'}
        widget = {'nombres_tutor', forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            if field == 'estado_tutor':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input'
            })

            #Asignando nombres de funciones dependiendo el tipo de campo y si es requerido.
            required = self.fields[field].required
            if required:
                self.fields[field].widget.attrs.update({
                    'onblur':'isRequeried({});'.format('id_'+field)
                })
            if type(self.fields[field])==forms.EmailField:
                self.fields[field].widget.attrs.update({
                    'onblur':'isEmail({});'.format('id_'+field)
                })

            if field == 'telefono_tutor':
                self.fields[field].widget.attrs.update({
                    'placeholder':'45002585',
                    'onblur':'isTelephoneNumber({});'.format('id_'+field),
                })

            if field == 'DPI_tutor':
                self.fields[field].widget.attrs.update({
                    'placeholder':'0000 00000 0000',
                    'onblur':'isIdentify({});'.format(field),
                })

            if field == 'fecha_nacimiento_tutor':
                self.fields[field].widget.attrs.update({
                    'placeholder':'dd/mm/yyyy',
                    'type':'date',
                })

        self.fields['genero'].empty_label = "Seleccione Genero"
        self.fields['parentesco'].empty_label = "Seleccione Parentesco"
