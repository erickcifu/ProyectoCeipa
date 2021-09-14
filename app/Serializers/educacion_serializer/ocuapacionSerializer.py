from rest_framework import serializer
from app.models.educacion_model import ocupacion


class ocupacionRegistroSerializer(serializer.serializer):
    nombre_ocupacion = serializers.CharField()

class ocupacionSerializer(serializers.ModelSerializer):
    class Meta:
        model =ocupacion
        fields=(
        'id',
        'nombre_ocupacion',
        'descripcion_ocupacion',
        'estado_ocupacion'
        )
