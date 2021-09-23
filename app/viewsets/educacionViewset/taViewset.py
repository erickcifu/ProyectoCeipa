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

from app.models import tarea_alumno
from app.serializer import TARegistroSerializer, TASerializer
from app.models import Alumno
from app.models import tarea


class TAViewset(viewsets.ModelViewSet):
    queryset = tarea_alumno.objects.filter(estado_tareaAlumno=True)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("tarea__titulo_tarea","estado_tareaAlumno")
    search_fields = ("tarea__titulo_tarea","estado_tareaAlumno")
    ordering_fields = ("tarea__titulo_tarea","estado_tareaAlumno")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return TASerializer
        else:
            return TARegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = TARegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    tarea = tarea.objects.get(pk=data.get("tarea"))
                    alumno = Alumno.objects.get(pk=data.get("Alumno"))
                    tarea_alumno.objects.create(
                        tarea = tarea,
                        alumno = alumno,
                        nota_obtenida = data.get("nota_obtenida"),
                        observaciones = data.get("observaciones"),
                        estado_entrega = data.get("estado_entrega"),
                    )
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        try:
            data = request.data
            serializer = TARegistroSerializer
            with transaction.atomic():
                if serializer.is_valid():
                    tarea_alumno = tarea_alumno.objects.get(pk = pk)
                    tarea_alumno.tarea = tarea.objects.get(pk=data.get("tarea"))
                    tarea_alumno.alumno = Alumno.objets.get(pk=data.get("alumno"))
                    tarea_alumno.nota_obtenida = data.get("nota_obtenida")
                    tarea_alumno.observaciones = data.get("observaciones")
                    tarea_alumno.estado_entrega = data.get("estado_entrega")
                    tarea_alumno.save()

                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
