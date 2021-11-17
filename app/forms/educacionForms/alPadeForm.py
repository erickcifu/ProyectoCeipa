from django import forms
from app.models import Apadecimiento,Padecimiento


class APadeForm(forms.ModelForm):
    #padecimiento = forms.ModelMultipleChoiceField(queryset=Padecimiento.objects.all())
    estado_Alpadecimiento = forms.BooleanField()
    class Meta:
        model = Apadecimiento
        fields = ['padecimiento','tratamiento', 'estado_Alpadecimiento']
        labels = {'padecimiento':"AlumPad", 'tratamiento':'Tratamiento','estado_Alpadecimiento':"Estado"}
        widget = {'estado_Alpadecimiento': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'required': False
            })
            if field == 'estado_Alpadecimiento':
                self.fields[field].widget.attrs.update({
                'class':'form-check-input',
                'checked':True
            })
            if type(self.fields[field])==forms.BooleanField:
                self.fields[field].widget.attrs.update({
                    'class':'form-check-input'
            })
        self.fields['padecimiento'].empty_label = "Seleccione un padecimiento"
