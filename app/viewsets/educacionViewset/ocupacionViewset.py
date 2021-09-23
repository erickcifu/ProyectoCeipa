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

from app.models import ocupacion
from app.serializer import ocupacionRegistroSerializer, OcupacionSerializer

class OcupacionViewset(viewsets.ModelViewSet):
    queryset = ocupacion.objects.filter(estado_ocupacion=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre_ocupacion","descripcion_ocupacion")
    search_fields = ("nombre_ocupacion","descripcion_ocupacion")
    ordering_fields = ("nombre_ocupacion","descripcion_ocupacion")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return OcupacionSerializer
        else:
            return ocupacionRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]
