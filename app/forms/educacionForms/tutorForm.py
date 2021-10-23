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
    fecha_nacimiento = forms.DateField(
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
        fields = ['nombres_tutor', 'apellidos_tutor', 'DPI', 'fecha_nacimiento', 'direccion_tutor', 'telefono', 'correo', 'fotografia_t', 'muni', 'genero', 'parentesco', 'estado_tutor']
        labels = {'nombres_tutor':'Nombres', 'apellidos_tutor':'Apellidos', 'DPI':"DPI", 'fecha_nacimiento':'Fecha de nacimiento', 'direccion_tutor':'Direccion', 'telefono':"Telefono", 'correo':"Correo", 'fotografia_t':"Fotografia", 'muni':"Municipio", 'genero':"Genero", 'parentesco':'Parentesco', 'estado_tutor':'Estado'}
        widget = {'nombres_tutor', forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['genero'].empty_label = "Seleccione Genero"
        self.fields['parentesco'].empty_label = "Seleccione Parentesco"
