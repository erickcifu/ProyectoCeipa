import json
from django.db import transaction
from django.core.files import File
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters, viewsets
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings

from app.models import Alumno
from app.serializer import AlumnoRegistroSerializer, AlumnoSerializer
from app.models import ocupacion
from app.models import Tutor
from app.models import etnia
from app.models import idioma
from app.models import EstudiosAnt
from app.models import municipio
from app.models import genero


class AlumnoViewset(viewsets.ModelViewSet):
    queryset = Alumno.objects.filter(estado_alumno=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("tutor__nombres_tutor","estado_alumno")
    search_fields = ("tutor__nombres_tutor","estado_alumno")
    orderinf_fields = ("tutor__nombres_tutor","estado_alumno")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return AlumnoSerializer
        else:
            return AlumnoRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = AlumnoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    ocup = ocupacion.objects.get(pk=data.get("ocupacion"))
                    tutor = Tutor.objects.get(pk=data.get("Tutor"))
                    etni = etnia.objects.get(pk=data.get("etnia"))
                    idiome = idioma.objects.get(pk=data.get("idioma"))
                    estudios_anteriores = EstudiosAnt.objects.get(pk=data.get("EstudiosAnt"))
                    muni = municipio.objects.get(pk=data.get("municipio"))
                    gen = genero.objects.get(pk=data.get("genero"))
                    Alumno.objects.create(
                        ocup = ocup,
                        tutor = tutor,
                        etni = etni,
                        idiome = idiome,
                        estudios_anteriores = estudios_anteriores,
                        muni = muni,
                        gen = gen,
                        nombres_alumno = data.get("nombres_alumno"),
                        cui = data.get("cui"),
                        apellidos_alumno = data.get("apellidos_alumno"),
                        codigo_mineduc = data.get("codigo_mineduc"),
                        fecha_nacimiento = data.get("fecha_nacimiento"),
                        ingreso_familiar = data.get("ingreso_familiar"),
                        direccion_alumno = data.get("direccion_alumno"),
                        telefono = data.get("telefono"),
                        fotografia = data.get("fotografia"),
                        estado_alumno = data.get("estado_alumno"),
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = AlumnoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    alumno = Alumno.objects.get(pk = pk)
                    alumno.ocup = ocupacion.objects.get(pk=data.get("ocup"))
                    alumno.tutor = Tutor.objets.get(pk=data.get("tutor"))
                    alumno.etni = etnia.objects.get(pk=data.get("etni"))
                    alumno.idiome = idioma.objets.get(pk=data.get("idiome"))
                    alumno.estudios_anteriores = EstudiosAnt.objects.get(pk=data.get("estudios_anteriores"))
                    alumno.muni = municipio.objets.get(pk=data.get("muni"))
                    alumno.gen = genero.objects.get(pk=data.get("gen"))
                    alumno.nombres_alumno = data.get("nombres_alumno")
                    alumno.cui = data.get("cui")
                    alumno.apellidos_alumno = data.get("apellidos_alumno")
                    alumno.codigo_mineduc = data.get("codigo_mineduc")
                    alumno.fecha_nacimiento = data.get("fecha_nacimiento")
                    alumno.ingreso_familiar = data.get("ingreso_familiar")
                    alumno.direccion_alumno = data.get("direccion_alumno")
                    alumno.telefono = data.get("telefono")
                    alumno.fotografia = data.get("fotografia")
                    alumno.estado_alumno = data.get("estado_alumno")
                    alumno.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
