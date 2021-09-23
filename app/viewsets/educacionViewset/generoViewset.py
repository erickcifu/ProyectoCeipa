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

from app.models import genero
from app.serializer import generoRegistroSerializer, generoSerializer

class GeneroViewset(viewsets.ModelViewSet):
    queryset = genero.objects.filter(estado_genero=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("genero","estado_genero")
    search_fields = ("genero","estado_genero")
    ordering_fields = ("genero","estado_genero")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return generoSerializer
        else:
            return generoRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = generoRegistroSerializer(data=data)
            with transaction.atomic():
                if serializer.is_valid():
                    genero.objects.create(
                        genero = data.get("genero"),
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = generoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    genero = genero.objects.get(pk = pk)
                    genero.genero = data.get("genero")
                    genero.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
