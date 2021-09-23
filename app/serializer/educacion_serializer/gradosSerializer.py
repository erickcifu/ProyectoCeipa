from rest_framework import serializers
from app.models import grados

class gradosRegistroSerializer(serializers.Serializer):
    nombre_grados = serializers.CharField()

class GradosSerializer(serializers.ModelSerializer):
    class Meta:
        model = grados
        fields=(
        'id',
        'nombre_grados',
        'descripcion_grados',
        'estado_grados',
        )
