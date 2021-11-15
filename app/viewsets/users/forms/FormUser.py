from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.forms import widgets
from app.models.educacion_model.Perfil import Perfil
from app.models.educacion_model.Rol import Rol
from django.db import IntegrityError, transaction

class UserFormCoordinadorGeneral(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(
        attrs={'class':'form-control',
            'placeholder':'Ingrese contraseña...',
            'id':'password1',
            'required':'required'
        }
    ))
    password2 = forms.CharField(label='Contraseña de Confirmación', widget=forms.PasswordInput(
        attrs={'class':'form-control',
            'placeholder':'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required'
        }
    ))

    phone = forms.CharField(label='Número de teléfono', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Telefono',
            'id':'phone',
            'name':'phone',
            'required':'required'
        }
    ))
    address = forms.CharField(label='Dirección domiciliar', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Dirección',
            'id':'address',
            'name':'address',
            'required':'required'
        }
    ))

    rol = forms.ModelChoiceField(queryset=Rol.objects.filter(id__in=[1,2,7,8,10,11])
        # ,widget = forms.TextInput(
        #     attrs={
        #         'class':'form-control',
        #         'placeholder':'Cargo',
        #         'id':'rol',
        #         'name':'rol',
        #         'required':'required'
        #     }
        # )
    )

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
                print(user)
                perfil = Perfil(user=user,
                                phone=self.cleaned_data.get('phone'),
                                address=self.cleaned_data.get('address'),
                                rol = self.cleaned_data.get('rol')
                            )
                perfil.save()
        return user

class UserFormDirectorOAsistenteGeneral(forms.ModelForm):
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

    rol = forms.ModelChoiceField(queryset=Rol.objects.filter(id__in=[3,4]))

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
                print(user)
                perfil = Perfil(user=user,
                                phone=self.cleaned_data.get('phone'),
                                address=self.cleaned_data.get('address'),
                                rol = self.cleaned_data.get('rol')
                            )
                perfil.save()
        return user

#form para crear nuevos usuarios con los roles: asitente educacion, director y maestro.

class UserFormAsignarRolesCoordinadorEducacion(forms.ModelForm):
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

    rol = forms.ModelChoiceField(queryset=Rol.objects.filter(id__in=[2]))

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
                print(user)
                perfil = Perfil(user=user,
                                phone=self.cleaned_data.get('phone'),
                                address=self.cleaned_data.get('address'),
                                rol = self.cleaned_data.get('rol')
                            )
                perfil.save()
        return user

#form para crear equipo tecnico municipal y asistente
class UserFormEquipoMunicipalAsisenteMunicipal(forms.ModelForm):
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

    rol = forms.ModelChoiceField(queryset=Rol.objects.filter(id__in=[8,9]))

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
                print(user)
                perfil = Perfil(user=user,
                                phone=self.cleaned_data.get('phone'),
                                address=self.cleaned_data.get('address'),
                                rol = self.cleaned_data.get('rol')
                            )
                perfil.save()
        return user

#form para crear equipo socioproductivo y asitente
class UserFormEquipoSocioproductivoAsisenteSocioproductivo(forms.ModelForm):
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

    rol = forms.ModelChoiceField(queryset=Rol.objects.filter(id__in=[11,12]))

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
                print(user)
                perfil = Perfil(user=user,
                                phone=self.cleaned_data.get('phone'),
                                address=self.cleaned_data.get('address'),
                                rol = self.cleaned_data.get('rol')
                            )
                perfil.save()
        return user
