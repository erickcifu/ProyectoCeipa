from rest_framework import serializer
from app.models.educacion_model.grados import grados

class gradosRegistroSerializer(serializer.serializer):
    nombre_grados = serializers.CharField()

class gradosSerializer(serializers.ModelSerializer):
    class Meta:
        model = grados
        fields=(
        'id',
        'nombre_grados',
        'descripcion_grados',
        'estado_grados',
        )
