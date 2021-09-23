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

from app.models import Tutor
from app.serializer import TutorRegistroSerializer, TutorSerializer
from app.models import municipio
from app.models import genero
from app.models import Parentesco

class TutorViewset(viewsets.ModelViewSet):
    queryset = Tutor.objects.filter(estado_tutor=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = (
        "muni__nombre_municipio",
        "genero__genero",
        "parentesco__nombre_parentesco",
        "estado_tutor"
        )
    search_fields = (
        "muni__nombre_municipio",
        "genero__genero",
        "parentesco__nombre_parentesco",
        "estado_tutor"
        )
    orderinf_fields = (
        "muni__nombre_municipio",
        "genero__genero",
        "parentesco__nombre_parentesco",
        "estado_tutor"
        )

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return TutorSerializer
        else:
            return TutorRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]


    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = TutorRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    muni = municipio.objects.get(pk=data.get("municipio"))
                    genero = genero.objects.get(pk=data.get("genero"))
                    parentesco = Parentesco.objects.get(pk=data.get("parentesco"))
                    Tutor.objects.create(
                        muni = muni,
                        genero = genero,
                        parentesco = parentesco,
                        nombres_tutor = data.get("nombres_tutor"),
                        apellidos_tutor = data.get("apellidos_tutor"),
                        DPI = data.get("DPI"),
                        fecha_nacimiento = data.get("fecha_nacimiento"),
                        direccion_tutor = data.get("direccion_tutor"),
                        telefono = data.get("telefono"),
                        fotografia = data.get("fotografia"),
                        correo = data.get("correo"),
                        estado_tutor = data.get("estado_tutor"),
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = TutorRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    tutor = Tutor.objects.get(pk = pk)
                    tutor.muni = municipio.objects.get(pk=data.get("muni"))
                    tutor.genero = genero.objets.get(pk=data.get("genero"))
                    tutor.parentesco = Parentesco.objets.get(pk=data.get("parentesco"))
                    tutor.nombres_tutor = data.get("nombres_tutor")
                    tutor.apellidos_tutor = data.get("apellidos_tutor")
                    tutor.DPI = data.get("DPI")
                    tutor.fecha_nacimiento = data.get("fecha_nacimiento")
                    tutor.direccion_tutor = data.get("direccion_tutor")
                    tutor.telefono = data.get("telefono")
                    tutor.fotografia = data.get("fotografia")
                    tutor.correo = data.get("correo")
                    tutor.estado_tutor = data.get("estado_tutor")
                    tutor.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
