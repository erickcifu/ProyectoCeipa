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

from app.models import Ciclo
from app.serializer import cicloRegistroSerializer, cicloSerializer

class CicloViewset(viewsets.ModelViewSet):
    queryset = Ciclo.objects.filter(estado_ciclo=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("anio","estado_ciclo")
    search_fields = ("anio","estado_ciclo")
    ordering_fields = ("anio","estado_ciclo")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return cicloSerializer
        else:
            return cicloRegistroSerializer

    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = cicloRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    Ciclo.objects.create(
                        anio = data.get("anio"),
                    )
                    return response(serializer,data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = cicloRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    ciclo = ciclo.objects.get(pk = pk)
                    ciclo.anio = data.get("anio")
                    ciclo.save()
                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
