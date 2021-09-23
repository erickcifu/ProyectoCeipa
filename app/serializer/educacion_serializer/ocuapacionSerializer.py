from rest_framework import serializers
from app.models import ocupacion


class ocupacionRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ocupacion
        fields = (
            'nombre_ocupacion',
        )
class OcupacionSerializer(serializers.ModelSerializer):
    class Meta:
        model =ocupacion
        fields=(
            'id',
            'nombre_ocupacion',
            'descripcion_ocupacion',
            'estado_ocupacion'
        )
