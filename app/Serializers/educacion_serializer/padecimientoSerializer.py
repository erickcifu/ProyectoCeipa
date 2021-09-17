from rest_framework import serializer
from app.models.educacion_model.padecimientoModel import Padecimiento

class PadecimientoRegistroSerializer(serializer.serializer):
    padecimiento = serializers.CharField()


class PadecimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = psicologico
        fields=(
        'id',
        'pacimiento',
        'estado_padecimiento',
        )
