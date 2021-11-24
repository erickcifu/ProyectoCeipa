from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View
from django.db.models import Count, OuterRef, Subquery, IntegerField
from app.utils import render_to_pdf

from app.models import Alumno, ocupacion, genero, Inscripcion, Inscripcion_etapa, EstudiosAnt, Grado, Etapa, Ciclo, Ciclo_grado, Ciclo_etapa
from app.models.educacion_model.idioma import idioma
from app.models.educacion_model.municipioModel import municipio
from app.models.educacion_model.departamento import departamento
from app.models.educacion_model.etnia import etnia
from app.models.educacion_model.genero import genero
from app.models import BeneficiadoArea

from app.models.educacion_model.centro_educativo import centro_educativo

class ReportesAlumnospdf(View):
    model = Alumno
    template_name = 'reportespdf/alumnos_pdf.html'
    context_object_name = 'obj'

    def get(self, request, *args, **kwargs):
        Total_alumnos = Alumno.objects.filter(estado_alumno=True).count()
        Total_alumnos_etapas = Inscripcion_etapa.objects.filter(insc_etapa_estado=True).count()
        Total_alumnos_grados = Inscripcion.objects.filter(estado_incpripsion=True).count()
        Total_alumnos_repitentes = EstudiosAnt.objects.filter(repitente=True).count()
        alumnos_por_genero = genero.objects.filter(estado_genero=True).annotate(cant_por_genero = Count('G_genero'))
        Alumnos_por_edad = Alumno.objects.filter(estado_alumno=True).annotate(cantidad_edad=Count('edad')).order_by('edad')
        ocupa = ocupacion.objects.annotate(cantidad_ocup=Count('O_ocupacion__id'))
        alumnos_por_centro_educativo = centro_educativo.objects.filter(estado_centro=True).annotate(cantidad = Count('C_educativo__alumno__id'))
        alumnos_por_grado = Grado.objects.filter(estado_grado=True).annotate(cantidad_por_grado = Count('cg_grado__ciclo_grado'))
        alumnos_por_etapa = Etapa.objects.filter(estado_etapa=True).annotate(cantidad_por_etapa = Count('ce_etapa__ce_insc'))
        data = {
            'Total_alumnos':Total_alumnos,
            'Total_alumnos_etapas':Total_alumnos_etapas,
            'Total_alumnos_grados':Total_alumnos_grados,
            'Total_alumnos_repitentes':Total_alumnos_repitentes,
            'alumnos_por_genero':alumnos_por_genero,
            'Alumnos_por_edad':Alumnos_por_edad,
            'ocupacion':ocupa,
            'alumnos_por_centro_educativo':alumnos_por_centro_educativo,
            'alumnos_por_grado':alumnos_por_grado,
            'alumnos_por_etapa':alumnos_por_etapa
        }
        pdf = render_to_pdf('reportespdf/alumnos_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
