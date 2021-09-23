from rest_framework import serializers
from app.models import seccion

class seccionRegistroSerializer(serializers.Serializer):
    nombre_seccion = serializers.CharField(max_length=255)


class seccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = seccion
        fields=(
            'id',
            'nombre_seccion ',
            'estado_seccion',
        )
