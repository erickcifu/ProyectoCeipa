from rest_framework import serializer
from app.models.educacion_model.curso import Curso

class cursoRegistroSerializer(serializer.serializer):
    nombre_curso = serializers.CharField(max_length=100)
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
