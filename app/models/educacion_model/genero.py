from django.db import models

class genero(models.Model):
    genero = models.CharField(max_length=50,null=False)
    estado_genero = models.BooleanField(default=True)

    def delete(self, *args):
        self.estado_genero = False
        self.save()
        return True
