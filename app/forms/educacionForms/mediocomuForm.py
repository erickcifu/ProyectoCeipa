from django import forms
from app.models import MedioComuni, Persona, Cargo

class MedioComuniForm(forms.ModelForm):
    persona = forms.ModelChoiceField(
        queryset = Persona.objects.filter(estado_persona=True)
        .order_by('persona')
    )
    cargo = forms.ModelChoiceField(
        queryset = Cargo.objects.filter(estado_cargo=True)
        .order_by('nombre_cargo')
    )
    class Meta:
        model = MedioComuni
        fields = ['nombre_medio', 'correo', 'telefono', 'persona', 'cargo', 'estado']
        labels = {'nombre_medio':'Nombres', 'correo':'Correo', 'telefono':"Telefono", 'persona':'Persona', 'cargo':'Cargo', 'estado':'Estado'}
        widget = {'nombre_medio', forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['persona'].empty_label = "Seleccione Persona"
        self.fields['cargo'].empty_label = "Seleccione Cargo"