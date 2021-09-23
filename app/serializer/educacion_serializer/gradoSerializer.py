from rest_framework import serializers
from app.models import Grado

class GradoRegistroSerializer(serializers.Serializer):
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
