from rest_framework import serializer
from app.models.educacion_model.psicologicoModel import psicologico

class psicologicoRegistroSerializer(serializer.serializer):
    alumno = serializers.IntegerField()
    Analisis_psicologico = serializers.CharField()
    fecha_Analisis = serializer.DateTimeField()
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
