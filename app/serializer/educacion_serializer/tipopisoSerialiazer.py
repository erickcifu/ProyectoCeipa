from rest_framework import serializers
from app.models import Tipo_piso

class tipopisoRegistroSerializer(serializers.Serializer):
    tipo_piso = serializers.CharField()


class tipopisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_piso
        fields=(
            'id',
            'tipo_piso',
            'descripcion_tipopiso',
            'estado_tipopiso',
        )
        depth = 2
