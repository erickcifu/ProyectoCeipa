from rest_framework import serializer
from app.models.educacion_model.religion_alumno import Religion_alumno

class Religion_alumnoRegistroSerializer(serializer.ModelSerializer):
    class Meta:
        model = Religion_alumno
        fields = (
            'nombre_iglesia',
        )

class Religion_alumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion_alumno
        fields=(
        'id',
        'nombre_iglesia',
        'estado_religionalumno',
        )