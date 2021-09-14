from rest_framework import serializer
from app.models.educacion_model.estudiosantModel import EstudiosAnt

class estudiosantRegistroSerializer(serializer.serializer):
    grado = serializers.IntegerField()
    nombre_establecimiento = serializers.CharField()


class estudiosantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudiosAnt
        fields=(
        'id',
        'grado',
        'nombre_establecimiento',
        'repitente',
        'telefono',
        'estado_estudiosant',
        )
        depth = 2
