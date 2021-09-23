from rest_framework import serializers
from app.models import Padecimiento

class PadecimientoRegistroSerializer(serializers.Serializer):
    nombre_padecimiento = serializers.CharField(max_length=205)


class PadecimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Padecimiento
        fields=(
        'id',
        'nombre_padecimiento',
        'estado_padecimiento',
        )
