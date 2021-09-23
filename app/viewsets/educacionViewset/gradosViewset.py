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

from app.models.educacion_model.grados import grados
from app.serializer.educacion_serializer.gradosSerializer import gradosRegistroSerializer, GradosSerializer

class GradosViewset(viewsets.ModelViewSet):
    queryset = grados.objects.filter(estado_grados=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre_grados","estado_grados")
    search_fields = ("nombre_grados","estado_grados")
    ordering_fields = ("nombre_grados","estado_grados")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return GradosSerializer
        else:
            return gradosRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    #'''"""******************** CREATE *****************************"""'''
    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = gradosRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    grados.objects.create(
                        nombre_grados = data.get("nombre_grados"),
                        descripcion_grados = data.get("descripcion_grados"),
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    #"""******************** UPDATE *****************************"""
    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = gradosRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    grados = grados.objects.get(pk = pk)
                    grados.nombre_grados = data.get("nombre_grados")
                    grados.descripcion_grados = data.get("descripcion_grados")
                    grados.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
