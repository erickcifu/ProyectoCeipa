from rest_framework import serializer
from app.models.educacion_model.centro_educativo import centro_educativo

class centroRegistroSerializer(serializer.serializer):
    nombre_centro = serializers.CharField()
    codigo_centro = serializers.CharField()

class centroSerializer(serializers.ModelSerializer):
    class Meta:
        model = centro_educativo
        fields=(
        'id',
        'nombre_centro',
        'direccion_centro',
        'codigo_centro',
        'estado_centro',
        )
