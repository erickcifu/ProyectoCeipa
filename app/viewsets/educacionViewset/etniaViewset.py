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

from app.models import etnia
from app.serializer import EtniaRegistroSerializer, EtniaSerializer

class EtniaViewset(viewsets.ModelViewSet):
    queryset = etnia.objects.filter(estado_etnia=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre_etnia", "estado_etnia")
    search_fields = ("nombre_etnia", "estado_etnia")
    ordering_fields = ("nombre_etnia", "estado_etnia")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return EtniaSerializer
        else:
            return EtniaRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = EtniaRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    etnia.objects.create(
                        nombre_etnia = data.get("nombre_etnia"),
                        descripcion_etnia = data.get("descripcion_etnia"),
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = EtniaRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    etnia = etnia.objects.get(pk = pk)
                    etnia.etnia = data.get("etnia")
                    etnia.descripcion_etnia = data.get("descripcion_etnia")
                    etnia.estado_etnia = data.get("estado_etnia")
                    etnia.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
