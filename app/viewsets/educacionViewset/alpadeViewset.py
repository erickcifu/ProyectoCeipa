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

from app.models.educacion_model.alumnopadecimiento import Apadecimiento
from app.serializer.educacion_serializer.alpadecimientoSerializer import psicologicoRegistroSerializer, psicologicoSerializer
from app.serializer.educacion_serializer.padecimientoModelo import padecimiento
from app.serializer.educacion_serializer.alumnoModelo import Alumno


class AlPAViewset(viewsets.ModelViewset):
    queryset = Apadecimiento.objects.filter(estado_Alpadecimiento=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("padecimiento__padecimiento","estado_Alpadecimiento")
    search_fields = ("padecimiento__padecimiento","estado_Alpadecimiento")
    orderinf_fields = ("padecimiento__padecimiento","estado_Alpadecimiento")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return AlpadecimientoSerializer
        else:
            return AlpadecimientoRegistroSerializer
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
            serializer = AlpadecimientoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    padecimiento = Padecimiento.objects.get(pk=data.get("padecimiento"))
                    alumnos = Alumno.objects.get(pk=data.get("Alumno"))
                    Apadecimiento.objects.create(
                        padecimiento = padecimiento,
                        alumno = alumnos
                        tratamiento = data.get("tratamiento"),
                        lugar = data.get("lugar"),
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
            serializer = AlpadecimientoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    almpadecimiento = padecimiento.objects.get(pk = pk)
                    almpadecimiento.alumno = Alumno.objects.get(pk=data.get("Alumno"))
                    almpadedecimiento.tratamiento = tratamiento.objects.get(pk=data.get("tratamiento"))
                    almpadedecimiento.lugar = lugar.objets.get(pk=data.get("lugar"))
                    almpadedecimiento.save()

                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST
