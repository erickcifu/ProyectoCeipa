from rest_framework import serializers
from app.models import Tutor

class TutorRegistroSerializer(serializers.Serializer):
    muni = serializers.IntegerField()
    genero = serializers.IntegerField()
    parentesco = serializers.IntegerField()
    nombres_tutor = serializers.CharField()
    apellidos_tutor = serializers.CharField()
    DPI = serializers.IntegerField()
    fecha_nacimiento = serializers.DateField()
    direccion_tutor = serializers.CharField()
    telefono = serializers.CharField()
    fotografia = serializers.ImageField()
    correo = serializers.EmailField()
    estado_tutor = serializers.BooleanField()

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = (
            'id',
            'muni',
            'genero',
            'parentesco',
            'nombres_tutor',
            'DPI',
            'apellidos_tutor',
            'fecha_nacimiento',
            'direccion_tutor',
            'telefono',
            'fotografia',
            'correo',
            'estado_tutor',
        )
        depth = 2
