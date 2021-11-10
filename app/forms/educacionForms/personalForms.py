from django import forms
from app import models
from app.models import personalEducativo
from django.contrib.auth.models import User
from app.models.educacion_model.Perfil import Perfil
from django.db import transaction

class PersonalForm(forms.ModelForm):
    fechaNac_personal = forms.DateField(
        widget = forms.TextInput(
            attrs={'type':'date'}
        )
    )
    estado_personal = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                'checked':True,
            }
        ), required=False, label="Activo/Inactivo"
    )
    class Meta:
        model = personalEducativo
        fields = ['nombres', 'apellidos', 'telefono_personal', 'email_personal', 'fechaNac_personal', 'direccion_personal', 'certificadoRenas_personal', 'estado_personal']
        labels = {'nombres':'Nombres', 'apellidos':'Apellidos', 'telefono_personal':'Telefono', 'email_personal':'Email', 'fechaNac_personal':'Fecha', 'direccion_personal':'Direccion', 'certificadoRenas_personal':'Certificado', 'estado_personal':'Estado'}
        widget = {'nombres', forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })

class DirectorCentroForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={'class':'form-control',
            'placeholder':'Ingrese contraseña...',
            'id':'password1',
            'required':'required'
        }
    ))
    password2 = forms.CharField(label='Contraseña de Confirmacion', widget=forms.PasswordInput(
        attrs={'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required'
        }
    ))

    phone = forms.CharField(label='Numero de telefono', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Telefono',
            'id':'phone',
            'name':'phone',
            'required':'required'
        }
    ))
    address = forms.CharField(label='Direccion', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'direccion',
            'id':'address',
            'name':'address',
            'required':'required'
        }
    ))
    fechaNac_personal = forms.DateField(label='Fecha de nacimiento',
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
                'placeholder':'fecha nacimiento',
                'id':'fechaNac_personal',
                'name':'fechaNac_personal',
                'required':'required'
            }
        )
        )
    certificadoRenas_personal = forms.BooleanField(label='está Certificado?')
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')

        return password2

    def save(self, commit=True):
        user =  super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            with transaction.atomic():
                user.save()
                perfil = Perfil(user=user,
                                phone=self.cleaned_data.get('phone'),
                                address=self.cleaned_data.get('address'),
                                rol_id = 5
                            )
                perfil.save()
                personal = personalEducativo(
                    nombres=user.first_name or '',
                    apellidos=user.last_name or '',
                    telefono_personal = perfil.phone or '',
                    email_personal = user.email or None,
                    direccion_personal = perfil.address or '',
                    fechaNac_personal = self.cleaned_data.get('fechaNac_personal'),
                    certificadoRenas_personal = self.cleaned_data.get('certificadoRenas_personal'),
                    perfile = perfil
                    )
                personal.save()
        return user

class MaestroCentroForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={'class':'form-control',
            'placeholder':'Ingrese contraseña...',
            'id':'password1',
            'required':'required'
        }
    ))
    password2 = forms.CharField(label='Contraseña de Confirmacion', widget=forms.PasswordInput(
        attrs={'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required'
        }
    ))

    phone = forms.CharField(label='Numero de telefono', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Telefono',
            'id':'phone',
            'name':'phone',
            'required':'required'
        }
    ))
    address = forms.CharField(label='Direccion', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'direccion',
            'id':'address',
            'name':'address',
            'required':'required'
        }
    ))
    fechaNac_personal = forms.DateField(label='Fecha de nacimiento',
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
                'placeholder':'fecha nacimiento',
                'id':'fechaNac_personal',
                'name':'fechaNac_personal',
                'required':'required'
            }
        )
        )
    certificadoRenas_personal = forms.BooleanField(label='está Certificado?')

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')

        return password2

    def save(self, commit=True):
        user =  super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            with transaction.atomic():
                user.save()
                perfil = Perfil(user=user,
                                phone=self.cleaned_data.get('phone'),
                                address=self.cleaned_data.get('address'),
                                rol_id = 6
                            )
                perfil.save()
                personal = personalEducativo(
                    nombres=user.first_name or '',
                    apellidos=user.last_name or '',
                    telefono_personal = perfil.phone or '',
                    email_personal = user.email or None,
                    direccion_personal = perfil.address or '',
                    fechaNac_personal = self.cleaned_data.get('fechaNac_personal'),
                    certificadoRenas_personal = self.cleaned_data.get('certificadoRenas_personal'),
                    perfile = perfil
                    )
                personal.save()
        return user,personal
