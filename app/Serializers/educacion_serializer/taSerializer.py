from rest_framework import serializer
from app.models.educacion_model.tarea_alumno import tarea_alumno

class TARegistroSerializer(serializer.serializer):
    tarea = serializers.IntegerField()
    alumno = serializers.IntegerField()
    nota_obtenida = serializers.FloatField()

class TASerializer(serializers.ModelSerializer):
    class Meta:
        model = tarea_alumno
        fields=(
        'id',
        'tarea',
        'alumno',
        'nota_obtenida',
        'observaciones',
        'estado_entrega',
        'estado_tareaAlumno',
        )
