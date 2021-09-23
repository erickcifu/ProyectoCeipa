from rest_framework import serializers
from app.models import centro_educativo

class centroRegistroSerializer(serializers.Serializer):
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
