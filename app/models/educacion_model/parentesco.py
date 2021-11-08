from django.db import models

class Parentesco(models.Model):
    nombre_parentesco = models.CharField(max_length=50, null=False)
    estado_parentesco = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_parentesco

    def delete(self, *args):
        self.estado_parentesco = False
        self.save()
        return True
