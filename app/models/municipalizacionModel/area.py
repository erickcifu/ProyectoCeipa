from django.db import models

class Area(models.Model):
    nombre_area= models.CharField(max_length=55,null=False)
    estado_area = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_area

    def delete(self, *args):
        self.estado_area = False
        self.save()
        return True
