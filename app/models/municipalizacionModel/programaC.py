from django.db import models

class ProgramaC(models.Model):
    nombre_programa = models.CharField(max_length=255, null=False)
    estado_programa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_programa

    def delete(self, *args):
        self.estado_programa = False
        self.save()
        return True
