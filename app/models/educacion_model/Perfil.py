from django.db import models
from django.contrib.auth.models import User
from app.models.educacion_model.Rol import Rol

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    avatar = models.ImageField(upload_to='Avatar', null=True, blank=True)
    phone = models.CharField(max_length=8, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='rol_profile')
    password_change = models.BooleanField(default=False, verbose_name='cammbio de contraseña por primera vez')
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username
    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    def delete(self, *args):
        user = self.user
        user.is_active = False
        user.save()
        self.active = False
        self.save()
        return True
