from rest_framework import serializers
from app.models import Ciclo_grado_curso

class cgcRegistroSerializer(serializers.Serializer):
    maestro = serializers.IntegerField()
    curso = serializers.IntegerField()
    ciclo_grado = serializers.IntegerField()

class cgcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciclo_grado_curso
        fields=(
            'id',
            'maestro',
            'curso',
            'ciclo_grado',
            'estado_cgc',
        )
        depth = 2
