from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from app.viewsets.users.directorGeneral.mixin import IsDirectorGeneralMixin
from app.viewsets.users.CoordinadorEducacion.mixin import IsCoordinadorEducacionMixin
from app.models import Alumno, ocupacion, genero, Inscripcion, Inscripcion_etapa, EstudiosAnt, Grado, Etapa, Ciclo, Ciclo_grado, Ciclo_etapa
from django.db.models import Count

from app.models.educacion_model.centro_educativo import centro_educativo

class ReportesAlumnosGeneral(IsDirectorGeneralMixin, generic.ListView):
    model = Alumno
    template_name = 'directorGeneral/alumnos.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Total_alumnos'] = Alumno.objects.filter(estado_alumno=True).count()
        context['Total_alumnos_etapas'] = Inscripcion_etapa.objects.filter(insc_etapa_estado=True).count()
        context['Total_alumnos_grados'] = Inscripcion.objects.filter(estado_incpripsion=True).count()
        context['Total_alumnos_repitentes'] = EstudiosAnt.objects.filter(repitente=True).count()
        context['alumnos_por_genero'] = genero.objects.filter(estado_genero=True).annotate(cant_por_genero = Count('G_genero'))
        context['Alumnos_por_edad'] = Alumno.objects.filter(estado_alumno=True).annotate(cantidad_edad=Count('edad')).order_by('edad')
        context['ocupacion'] = ocupacion.objects.annotate(cantidad_ocup=Count('O_ocupacion__id'))
        context['alumnos_por_centro_educativo'] = centro_educativo.objects.filter(estado_centro=True).annotate(cantidad = Count('C_educativo__alumno__id'))
        context['alumnos_por_grado'] = Grado.objects.filter(estado_grado=True).annotate(cantidad_por_grado = Count('cg_grado__ciclo_grado'))
        context['alumnos_por_etapa'] = Etapa.objects.filter(estado_etapa=True).annotate(cantidad_por_etapa = Count('ce_etapa__ce_insc'))
        return context
