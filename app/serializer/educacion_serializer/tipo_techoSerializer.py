from rest_framework import serializers
from app.models import Tipo_techo

class Tipo_techoRegistroSerializer(serializers.Serializer):
    tipo_techo = serializers.CharField()

class Tipo_techoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_techo
        fields = (
            'id',
            'tipo_techo',
            'descripcion_techo',
            'estado_techo',
        )
        depth = 2
