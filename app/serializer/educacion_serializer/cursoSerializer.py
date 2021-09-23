from rest_framework import serializers
from app.models import Curso

class cursoRegistroSerializer(serializers.Serializer):
    nombre_curso = serializers.CharField(max_length=100)
    descripcion_curso =serializers.CharField(max_length=255)
    grado = serializers.IntegerField()
class cursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields=(
            'id',
            'nombre_curso',
            'descripcion_curso',
            'grado',
            'estado_curso'
        )
        depth = 2
