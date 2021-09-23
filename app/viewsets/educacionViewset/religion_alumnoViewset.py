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
from app.models import Religion_alumno
from app.serializer import Religion_alumnoRegistroSerializer, Religion_alumnoSerializer

class Religion_alumnoViewset(viewsets.ModelViewSet):
    queryset = Religion_alumno.objects.filter(estado_religionalumno=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("religion__nombre_religion","estado_religionalumno")
    search_fields = ("religion__nombre_religion","estado_religionalumno")
    ordering_fields = ("religion__nombre_religion","estado_religionalumno")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return Religion_alumnoSerializer
        else:
            return Religion_alumnoRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]
    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = Religion_alumnoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    religion = religion.objects.get(pk=data.get("religion"))
                    alumnos = Alumno.objects.get(pk=data.get("Alumno"))
                    Religion_alumno.objects.create(
                        religion = religion,
                        alumno = alumnos,
                        nombre_iglesia = data.get("nombre_iglesia"),
                        estado_religionalumno = data.get("estado_religionalumno"),
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = Religion_alumnoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    religion_alumno = Religion_alumno.objects.get(pk = pk)
                    religion_alumno.alumno = Alumno.objects.get(pk=data.get("Alumno"))
                    religion_alumno.religion = religion.objects.get(pk=data.get("religion"))
                    religion_alumno.nombre_iglesia = data.get("nombre_iglesia")
                    religion_alumno.estado_religionalumno = data.get("estado_religionalumno")
                    religion_alumno.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
