from django.db import models
from app.models import Perfil

class personalEducativo(models.Model):
    nombres = models.CharField(max_length=255,null=False)
    apellidos = models.CharField(max_length=255, null=False)
    perfile = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='profile_personalEducativo')
    telefono_personal = models.CharField(max_length=15,null=True, blank=True)
    email_personal = models.CharField(max_length=50,null=True, blank=True)
    fechaNac_personal = models.DateTimeField()
    direccion_personal = models.CharField(max_length=255,null=True, blank=True)
    certificadoRenas_personal = models.BooleanField(default=False, null=False)
    estado_personal = models.BooleanField(default=True)

    def __str__(self):
        return self.nombres

    def delete(self, *args):
        self.estado_personal = False
        self.save()
        return True
