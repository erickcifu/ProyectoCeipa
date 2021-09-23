from rest_framework import serializers
from app.models import psicologico

class psicologicoRegistroSerializer(serializers.Serializer):
    alumno = serializers.IntegerField()
    Analisis_psicologico = serializers.CharField()
    fecha_Analisis = serializers.DateTimeField()
    Entrevistador = serializers.CharField()

class psicologicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = psicologico
        fields=(
            'id',
            'alumno',
            'Analisis_psicologico',
            'tratamiento',
            'Entrevistador',
            'fecha_Analisis',
            'estado_psicologico',
        )
        depth = 2
