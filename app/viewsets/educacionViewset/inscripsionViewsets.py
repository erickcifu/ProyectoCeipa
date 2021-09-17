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

from app.models.educacion_model.inscripsionModel import Inscripcion
from app.serializer.educacion_serializer.inscripsionSerializer import InscRegistroSerializer, InscSerializer
from app.models.educacion_model.centro_educativo import centro_educativo
from app.models.educacion_model.alumnoModelo import Alumno
from app.models.educacion_model.ciclo_grado import Ciclo_grado


class InViewset(viewsets.ModelViewset):
    queryset = tarea_alumno.objects.filter(estado_tareaAlumno=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("Alumno__nombre_alumno","estado_inscripsion","centro_educativo")
    search_fields = ("Alumno__nombre_alumno","estado_inscripsion","centro_educativo")
    orderinf_fields = ("Alumno__nombre_alumno","estado_inscripsion","centro_educativo")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return InscSerializer
        else:
            return InscRegistroSerializer
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
            serializer = InscRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    centro_educativo = centro_educativo.objects.get(pk=data.get("centro_educativo"))
                    alumno = Alumno.objects.get(pk=data.get("Alumno"))
                    ciclo_grado = ciclo_grado.objects.get(pk=data.get("ciclo_grado"))
                    Inscripcion.objects.create(
                        centro_educativo = centro_educativo,
                        alumno = alumno,
                        ciclo_grado = ciclo_grado,
                        Fecha_inscripcion = data.get("Fecha_inscripcion"),
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
            serializer = InscRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    inscripsion = inscripsion.objects.get(pk = pk)
                    inscripsion.centro_educativo = centro_educativo.objects.get(pk=data.get("centro_educativo"))
                    tarea_alumno.alumno = Alumno.objets.get(pk=data.get("alumno"))
                    inscripsion.ciclo_grado = ciclo_grado.objects.get(pk=data.get("ciclo_grado"))
                    inscripsion.Fecha_inscripcion = data.get("Fecha_inscripcion")
                    inscripsion.save()

                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST
