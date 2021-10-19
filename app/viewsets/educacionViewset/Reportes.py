from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Alumno, ocupacion
from django.db.models import Count

from app.models.educacion_model.centro_educativo import centro_educativo

class ReportesAlumnos(LoginRequiredMixin, generic.ListView):
    model = Alumno
    template_name = 'reportes/alumnos.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Masculino'] = Alumno.objects.filter(estado_alumno=True, gen__genero = 'Masculino').count()
        context['Femenino'] = Alumno.objects.filter(estado_alumno=True, gen__genero = 'Femenino').count()
        context['Alumnos_por_edad'] = Alumno.objects.filter(estado_alumno=True).annotate(cantidad=Count('edad')).order_by('edad')
        context['ocupacion'] = ocupacion.objects.annotate(cantidad=Count('O_ocupacion__id'))
        context['alumnos_por_centro_educativo'] = centro_educativo.objects.annotate(cantidad = Count('C_educativo__alumno__id'))
        return context
class CantidadAlumnosPorGenero(LoginRequiredMixin, generic.ListView):
    model = Alumno
    template_name = 'educacion/reportes/canditadAlumnosPorGenero.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Masculino'] = Alumno.objects.filter(estado_alumno=True, gen__genero = 'Masculino').count()
        context['Femenino'] = Alumno.objects.filter(estado_alumno=True, gen__genero = 'Femenino').count()

class AlumnosPorEdad(LoginRequiredMixin, generic.ListView):
    model = Alumno
    template_name = 'educacion/reportes/canditadAlumnosPorGenero.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Alumnos_por_edad'] = Alumno.objects.filter(estado_alumno=True).order_by('edad')

class AlumnosPorOcupacion(LoginRequiredMixin, generic.ListView):
    model = ocupacion
    template_name = 'educacion/reportes/canditadAlumnosPorGenero.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ocupacion'] = self.model.objects.annotate(cantidad=Count('O_ocupacion__id'))

class CantidadAlumnosPorCentro(LoginRequiredMixin, generic.ListView):
    model = centro_educativo
    template_name = 'educacion/reportes/canditadAlumnosPorGenero.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alumnos_por_centro_educativo'] = centro_educativo.objects.annotate(cantidad = Count('C_educativo_alumno__id'))
