from rest_framework import serializer
from app.models.educacion_model.alumnoModelo import Alumno

class AlumnoRegistroSerializer(serializer.serializer):
    ocup = serializers.IntegerField()
    tutor = serializers.IntegerField()
    etni = serializers.IntegerField()
    idiome = serializers.IntegerField()
    estudios_anteriores = serializers.IntegerField()
    muni = serializers.IntegerField()
    gen = serializers.IntegerField()
    religion = serializers.IntegerField()
    nombres_alumno = serializers.CharField()
    cui = serializers.IntegerField()
    apellidos_alumno = serializers.CharField()
    codigo_mineduc = serializers.IntegerField()
    fecha_nacimiento = serializers.DateField()
    ingreso_familiar = serializers.FloatField()
    direccion_alumno = serializers.CharField()
    telefono = serializers.CharField()
    fotografia = serializers.ImageField()
    estado_alumno = serializers.BooleanField()

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = (
            'id',
            'ocup',
            'tutor',
            'etni',
            'idiome',
            'estudios_anteriores',
            'muni',
            'gen',
            'religion',
            'nombres_alumno',
            'cui',
            'apellidos_alumno',
            'codigo_mineduc',
            'fecha_nacimiento',
            'ingreso_familiar',
            'direccion_alumno',
            'telefono',
            'fotografia',
            'estado_alumno',
        )
        depth = 2
