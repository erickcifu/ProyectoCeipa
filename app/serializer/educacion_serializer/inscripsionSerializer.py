from rest_framework import serializers
from app.models import Inscripcion

class InscRegistroSerializer(serializers.Serializer):
     centro_educativo = serializers.CharField(max_length=50)
     alumno = serializers.IntegerField()
     ciclo_grado = serializers.IntegerField()
     Fecha_inscripcion = serializers.DateTimeField()

class InscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields=(
        'id',
        'centro_educativo',
        'alumno',
        'ciclo_grado',
        'Fecha_inscripcion',
        'estado_incpripsion',
        )
        depth = 2
