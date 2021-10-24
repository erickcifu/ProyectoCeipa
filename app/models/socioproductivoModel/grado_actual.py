from django.db import models

class Grado_actual(models.Model):
    gradoact = models.CharField(max_length=150)
    estado_gradoact = models.BooleanField(default=True)

    def __str__(self):
        return self.gradoact

    def delete(self, *args):
        self.estado_gradoact = False
        self.save()
        return True
