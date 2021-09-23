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

from app.models.educacion_model.grado import Grado
from app.serializer.educacion_serializer.gradoSerializer import  GradoRegistroSerializer, GradoSerializer

class GradoViewset(viewsets.ModelViewSet):
    queryset = Grado.objects.filter(estado_grado=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre_grado", "estado_grado")
    search_fields = ("nombre_grado", "estado_grado")
    ordering_fields = ("nombre_grado", "estado_grado")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return GradoSerializer
        else:
            return GradoRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

        """******************** CREATE *****************************"""
    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = GradoRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    Grado.objects.create(
                        nombre_grado = data.get("nombre_grado"),
                        descripcion_grado = data.get("descripcion_grado"),
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

            """******************** UPDATE *****************************"""
    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = GradoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    Grado = Grado.objects.get(pk = pk)
                    Grado.nombre_grado = data.get("nombre_grado")
                    Grado.descripcion_grado = data.get("descripcion_grado")
                    Grado.estado_grado = data.get("estado_grado")
                    Grado.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
