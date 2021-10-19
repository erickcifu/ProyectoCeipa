from django import forms
from app.models import Apadecimiento,Padecimiento


class APadeForm(forms.ModelForm):
    #padecimiento = forms.ModelMultipleChoiceField(queryset=Padecimiento.objects.all())
    class Meta:
        model = Apadecimiento
        fields = ['padecimiento','tratamiento', 'estado_Alpadecimiento']
        labels = {'padecimiento':"AlumPad", 'estado_Alpadecimiento':"Estado"}
        widget = {'estado_Alpadecimiento': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
            self.fields['padecimiento'].empty_label = "Seleccione un padecimiento"
