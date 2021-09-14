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

from app.models.educacion_model.religion import religion
from app.serializer.educacion_serializer.religionSerializer import religionSerializer, religionRegistroSerializer


class religionViewset(viewsets.ModelViewset):
    queryset = religion.objects.filter(estado_religion=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre_religion","estado_religion")
    search_fields = ("nombre_religion","estado_religion")
    orderinf_fields = ("nombre_religion","estado_religion")

    def get_seralizer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
        else:
            return religionRegistroSerializer
    def get_permissions(self):
        if self.action == "creeate" or self.action == "token":
        else:
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]
