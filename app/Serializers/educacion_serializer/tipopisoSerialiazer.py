from rest_framework import serializer
from app.models.educacion_model.tipopisoModel import Tipo_piso

class tipopisoRegistroSerializer(serializer.serializer):
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
