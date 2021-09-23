from rest_framework import serializers
from app.models import Tipo_muro


class Tipo_muroRegistroSerializer(serializers.Serializer):
    tipo_muro = serializers.CharField()

class Tipo_muroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_muro
        fields = (
            'id',
            'tipo_muro',
            'descripcion_muro',
            'estado_muro',
        )
        depth = 2
