from rest_framework import serializers
from app.models import Religion_alumno

class Religion_alumnoRegistroSerializer(serializers.Serializer):
    religion = serializers.IntegerField()
    alumno = serializers.IntegerField()
    nombre_iglesia = serializers.CharField()

class Religion_alumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion_alumno
        fields=(
            'id',
            'religion',
            'alumno',
            'nombre_iglesia',
            'estado_religionalumno',
        )
        depth = 2
