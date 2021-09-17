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

from app.models.educacion_model.religion_alumno import Religion_alumno
from app.serializer.educacion_serializer.religion_alumnoSerializer import Religion_alumnoRegistroSerializer, Religion_alumnoSerializer
from app.models.educacion_model.religion import religion

class Religion_alumnoViewset(viewsets.ModelViewset):
    queryset = Religion_alumno.objects.filter(estado_religionalumno=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("religion__nombre_religion","estado_religionalumno")
    search_fields = ("religion__nombre_religion","estado_religionalumno")
    orderinf_fields = ("religion__nombre_religion","estado_religionalumno")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return Religion_alumnoSerializer
        else:
            return Religion_alumnoRegistroSerializer
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
            serializer = Religion_alumnoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    religion = religion.objects.get(pk=data.get("religion"))
                    Religion_alumno.objects.create(
                        religion = religion,
                        nombre_iglesia = data.get("nombre_iglesia"),
                        estado_religionalumno = data.get("estado_religionalumno"),
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
            serializer = Religion_alumnoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    religion_alumno = Religion_alumno.objects.get(pk = pk)
                    religion_alumno.religion = religion.objects.get(pk=data.get("religion"))
                    religion_alumno.nombre_iglesia = data.get("nombre_iglesia")
                    religion_alumno.estado_religionalumno = data.get("estado_religionalumno")
                    religion_alumno.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST