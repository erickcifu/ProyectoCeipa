from django.db import models

class Profesion(models.Model):
    nombre_profesion= models.CharField(max_length=55,null=False)
    estado_profesion = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_profesion

    def delete(self, *args):
        self.estado_profesion = False
        self.save()
        return True
