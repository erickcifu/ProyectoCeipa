from rest_framework import serializers
from app.models import Apadecimiento

class AlpadecimientoRegistroSerializer(serializers.Serializer):
    padecimiento = serializers.IntegerField()
    alumno = serializers.IntegerField()
    tratamiento = serializers.CharField()
    lugar = serializers.CharField()

class AlpadecimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apadecimiento
        fields=(
            'id',
            'padecimiento',
            'alumno',
            'tratamiento',
            'lugar',
            'estado_Alpadecimiento',
        )
        depth = 2
