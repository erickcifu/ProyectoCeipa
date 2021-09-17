import json
from django.core.files import File
from django_filters.rest_framework import djangoFilterBackend
from rest_framework import status, filters, viewsets
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings

from app.models.educacion_model.alumnoModelo import Alumno
from app.serializer.educacion_serializer.alumnoSerializer import AlumnoRegistroSerializer, AlumnoSerializer
from app.models.educacion_model.ocupacion import ocupacion
from app.models.educacion_model.tutor import Tutor
from app.models.educacion_model.etnia import etnia
from app.models.educacion_model.idioma import idioma
from app.models.educacion_model.estudiosantModel import EstudiosAnt
from app.models.educacion_model.municipioModel import municipio
from app.models.educacion_model.genero import genero
from app.models.educacion_model.religion_alumno import Religion_alumno

class AlumnoViewset(viewsets.ModelViewset):
    queryset = Alumno.objects.filter(estado_alumno=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = (
        "ocupacion__nombre_ocupacion",
        "Tutor__nombres_tutor",
        "etnia__nombre_etnia",
        "idioma__nombre_idioma",
        "EstudiosAnt__grado",
        "municipio__nombre_municipio",
        "genero__genero",
        "Religion_alumno__religion",
        "estado_alumno"
        )
    search_fields = (
        "ocupacion__nombre_ocupacion",
        "Tutor__nombres_tutor",
        "etnia__nombre_etnia",
        "idioma__nombre_idioma",
        "EstudiosAnt__grado",
        "municipio__nombre_municipio",
        "genero__genero",
        "Religion_alumno__religion",
        "estado_alumno"
        )
    orderinf_fields = (
        "ocupacion__nombre_ocupacion",
        "Tutor__nombres_tutor",
        "etnia__nombre_etnia",
        "idioma__nombre_idioma",
        "EstudiosAnt__grado",
        "municipio__nombre_municipio",
        "genero__genero",
        "Religion_alumno__religion",
        "estado_alumno"

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return AlumnoSerializer
        else:
            return AlumnoRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
        else:
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

"""******************** CREATE *****************************"""
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
                    religion = Religion_alumno.objects.get(pk=data.get("Religion_alumno"))
                    Alumno.objects.create(
                        ocup = ocup,
                        tutor = tutor,
                        etni = etni,
                        idiome = idiome,
                        estudios_anteriores = estudios_anteriores,
                        muni = muni,
                        gen = gen,
                        religion = religion,
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

"""******************** UPDATE *****************************"""
    def update(self,request,pk=none):
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
                    alumno.religion = Religion_alumno.objets.get(pk=data.get("religion"))
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
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST