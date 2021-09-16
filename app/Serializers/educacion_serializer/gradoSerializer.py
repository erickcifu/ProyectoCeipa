from rest_framework import serializer
from app.models.educacion_model.grado import Grado

class GradoRegistroSerializer(serializer.serializer):
    nombre_grado = serializers.CharField()

class GradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grado
        fields=(
            'id',
            'nombre_grado',
            'descripcion_grado',
            'estado_grado',
            )
        depth = 2
