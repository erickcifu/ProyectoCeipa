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

from app.models.educacion_model.seccionModelo import seccion
from app.serializer.educacion_serializer.seccionSerializer import seccionRegistroSerializer, seccionSerializer

class SeccionViewset(viewsets.ModelViewset):
    queryset = seccion.objects.filter(estado_seccion=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("nombre_seccion","estado_seccion")
    search_fields = ("nombre_seccion","estado_seccion")
    orderinf_fields = ("nombre_seccion","estado_seccion")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return seccionSerializer
        else:
            return seccionRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
        else:
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]
"""******************** Crear *************************************-"""
    def create(self,request, *args,**kwargs):
        try:
            data = request.data
            serializer = seccionRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    seccion.objects.create(
                    nombre_seccion = data.get("nombre_seccion"),
                    )
                    return response(serializer,data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
"""********************** ACTULIZAR ***************************"""
    def update(self,request,pk=none):
        try:
            data = request.data
            serializer = seccionRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    seccion= seccion.objects.get(pk = pk)
                    seccion.nombre_seccion = data.get("nombre_categoria"))
                    seccion.save()

                    return Response(serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
