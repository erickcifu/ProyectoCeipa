from rest_framework import serializers
from app.models import tarea

class tareaRegistroSerializer(serializers.Serializer):
    titulo_tarea = serializers.CharField(max_length=50)
    maestro = serializers.IntegerField()
    ciclo_grado_curso = serializers.IntegerField()
    nota_tarea = serializers.FloatField()
    fecha_entrega = serializers.DateTimeField()

class tareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tarea
        fields=(
            'id',
            'titulo_tarea',
            'descripcion_tarea',
            'maestro',
            'ciclo_grado_curso',
            'nota_tarea',
            'fecha_entrega',
            'estado_tarea',
        )
        depth = 2