from rest_framework import serializer
from app.models.educacion_model.personalEducativo import personalEducativo

class personalRegistroSerializer(serializer.serializer):
    nombres = serializers.CharField(max_length=255)
    apellidos = serializers.CharField(max_length=255)
    email_personal = serializers.CharField(max_length=50)
    fechaNac_personal = serializers.DateTimeField()
    certificadoRenas_personal = serializers.BooleanField(default=False)

class personalSerializer(serializers.ModelSerializer):
    class Meta:
        model = personalEducativo
        fields=(
        'id',
        'nombres',
        'apellidos',
        'telefono_personal',
        'email_personal',
        'fechaNac_personal',
        'direccion_personal',
        'certificadoRenas_personal',
        'estado_personal',
        )
        depth = 2
