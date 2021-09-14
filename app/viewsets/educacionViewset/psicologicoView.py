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

from app.models.educacion_model.psicologicoModelo import psicologico
from app.serializer.educacion_serializer.psicologicoSerializer import psicologicoRegistroSerializer, psicologicoSerializer
from app.models.educacion_model.alumnoModelo import Alumno

class psicologicoViewset(viewsets.ModelViewset):
    queryset = psicologico.objects.filter(estado_psicologico=True)
    filter_backends = (djangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields = ("alumno__nombre_alumno","estado_psicologico")
    search_fields = ("alumno__nombre_alumno","estado_psicologico")
    orderinf_fields = ("alumno__nombre_alumno","estado_psicologico")

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return psicologicoSerializer
        else:
            return psicologicoRegistroSerializer
    def get_permissions(self):
        if self.action == "create" or self.action == "token":
        else:
            permissions_classes = [AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]
            """******crear******-"""
    def create(self,request, *args,**kwargs):
        try:
            data = request.data
            serializer = psicologicoRegistroSerializer(data = data)
            with transaction.atomic():#detiene procesos si hay mas
                if serializer.is_valid():
                    alumnos = Alumno.objects.get(pk=data.get('Alumno'))
                    psicologico.objects.create(
                    alumno = alumnos,
                    Analisis_psicologico = data.get("Analisis_psicologico"),
                    tratamiento = data.get("tratamiento"),
                    fecha_Analisis = data.get("fecha_Analisis"),
                    Entrevistador = data.get("Entrevistador"),
                    )
                    return response(serializer,data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail":str(e)},status=status.HTTP_400_BAD_REQUEST)
            """****ACTULIZAR**************"""
    def update(self,request,pk=none):
        try:
            data = request.data
            serializer = psicologicoRegistroSerializer(data = data)
            with transaction.atomic():
                if serializer.is_valid():
                    psicologico = psicologico.objects.get(pk = pk)
                    psicologico.alumnos = psicologico.objects.get(pk-data.get("Alumno"))
                    psicologico.save()

                    return Response(serializer.data, status = status.HTTP_200_OK)
