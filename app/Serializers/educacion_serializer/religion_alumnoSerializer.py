from rest_framework import serializer
from app.models.educacion_model.religion_alumno import Religion_alumno

class Religion_alumnoRegistroSerializer(serializer.ModelSerializer):
    religion = serializers.IntegerField()
    nombre_iglesia = serializers.CharField()

class Religion_alumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion_alumno
        fields=(
            'id',
            'religion',
            'nombre_iglesia',
            'estado_religionalumno',
            )
        depth = 2
