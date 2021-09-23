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

from app.models import seccion
from app.serializer import seccionRegistroSerializer, seccionSerializer

class SeccionViewset(viewsets.ModelViewSet):
    queryset = seccion.objects.filter(estado_seccion=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre_seccion","estado_seccion")
    search_fields = ("nombre_seccion","estado_seccion")
    ordering_fields = ("nombre_seccion","estado_seccion")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return seccionSerializer
        else:
            return seccionRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    def create(self,request, *args,**kwargs):
        try:
            data = request.data
            serializer = seccionRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    seccion.objects.create(
                    nombre_seccion = data.get("nombre_seccion"),
                    )
                    return Response(serializer,data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = seccionRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    seccion= seccion.objects.get(pk = pk)
                    seccion.nombre_seccion = data.get("nnombre_seccion")
                    seccion.save()

                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
