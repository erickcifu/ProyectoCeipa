from django import forms
from app.models import MedioComuni, Persona, Cargo

class MedioComuniForm(forms.ModelForm):
    cargo = forms.ModelChoiceField(
        queryset = Cargo.objects.filter(estado_cargo=True)
        .order_by('nombre_cargo')
    )
    class Meta:
        model = MedioComuni
        fields = ['nombre_medio', 'correo', 'telefono', 'cargo', 'estado']
        labels = {'nombre_medio':'Nombres de el medio', 'correo':'Correo', 'telefono':"Telefono",  'cargo':'Cargo', 'estado':'Estado'}
        widget = {'nombre_medio', forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['cargo'].empty_label = "Seleccione Cargo"
