from rest_framework import serializer
from app.models.educacion_model.seccionModelo import seccion

class seccionRegistroSerializer(serializer.serializer):
    nombre_seccion = serializers.CharField()


class seccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = seccion
        fields=(
        'id',
        'nombre_seccion',
        'estado_seccion',
        )
        
