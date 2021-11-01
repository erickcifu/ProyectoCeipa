from django.db import models
from app.models.educacion_model.parentesco import Parentesco

class TutorMuni(models.Model):
    nombres_tutor = models.CharField(max_length=50,null=False)
    apellidos_tutor = models.CharField(max_length=50,null=True)
    DPI = models.CharField(max_length=13)
    fecha_nacimiento = models.DateField()
    direccion_tutor = models.CharField(max_length=80, null=True, blank=True)
    telefono = models.CharField(max_length=8, null=True, blank=True)
    fotografia_tutor = models.ImageField(upload_to='ceipa', null=True, blank=True)
    parentesco = models.ForeignKey(Parentesco, on_delete=models.CASCADE, related_name="T_parentesco")
    estado_tutor = models.BooleanField(default=True)

    @property
    def foto_url(self):
        if self.fotografia_tutor and hasattr(self.fotografia_tutor, 'url'):
            return self.fotografia_tutor.url

    def __str__(self):
        return self.nombres_tutor

    def delete(self, *args):
        self.estado_tutor = False
        if self.fotografia is not  None:
            self.fotografia.delete()
        self.save()
        return True
