from rest_framework import serializer
from app.models.educacion_model.alpadecimientoModel import Padecimiento

class AlpadecimientoRegistroSerializer(serializer.serializer):
    padecimiento = serializer.integerField()
    alumno = serializer.integerField()
    tratamiento = serializers.CharField()
    lugar = serializers.CharField()

class AlpadecimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model =
        fields=(
        'id',
        'padecimiento',
        'alumno',
        'tratamiento',
        'lugar',
        'estado_Alpadecimiento',
        )
        depth = 2
