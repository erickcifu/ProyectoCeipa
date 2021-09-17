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

from app.models.educacion_model.padecimientoModel import Padecimiento
from app.serializer.educacion_serializer.padecimientoSerializer import PadecimientoRegistroSerializer, PadecimientoSerializer


class PadecimientoViewset(viewsets.ModelViewset):
    queryset = Padecimiento.objects.filter(estado_padecimiento=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("Padecimiento","estado_padecimiento")
    search_fields = ("Padecimiento","estado_padecimiento")
    orderinf_fields = ("Padecimiento","estado_padecimiento")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PadecimientoSerializer
        else:
            return PadecimientoRegistroSerializer
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
            serializer = PadecimientoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    Padecimiento.objects.create(
                        Padecimiento = data.get("Padecimiento"),
                        estado_padecimiento = data.get("estado_padecimiento"),
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
            serializer = PadecimientoRegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    Padecimiento.padecimiento = data.get("padecimiento")
                    padecimiento.save()

                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST
