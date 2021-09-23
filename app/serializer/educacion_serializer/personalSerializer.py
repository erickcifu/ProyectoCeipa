from rest_framework import serializers
from app.models import personalEducativo

class personalRegistroSerializer(serializers.Serializer):
    nombres = serializers.CharField(max_length=255)
    apellidos = serializers.CharField(max_length=255)
    email_personal = serializers.CharField(max_length=50)
    fechaNac_personal = serializers.DateTimeField()
    certificadoRenas_personal = serializers.BooleanField(default=False)
'''
    class Meta:
        model = personalEducativo
        fields=(
            'nombres',
            'apellidos',
            'email_personal',
            'fechaNac_personal',
            'certificadoRenas_personal',
        )
'''
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
