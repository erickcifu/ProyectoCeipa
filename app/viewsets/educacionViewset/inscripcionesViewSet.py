from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Inscripcion_etapa, Alumno, centro_educativo, Ciclo_etapa, Ciclo
from app.forms import InscEtapaForm
from datetime import datetime


#listando los maestros por centro educativo
class ListarAlumnosParaCentro(LoginRequiredMixin, generic.ListView):
    model = Alumno
    template_name = 'educacion/alumnos_list_etapas_por_centro.html'
    context_object_name = 'obj'

    def get_queryset(self):
        id_centro_educativo = self.request.GET.get("id_centro_educativo")
        if id_centro_educativo:
            return Alumno.objects.filter(insc_alumn_etapa__centro_educ_etapa_id=int(id_centro_educativo))

        return Alumno.objects.filter(insc_alumn_etapa__centro_educ_etapa_id__in=centro_educativo.objects.filter(estado_centro=True).values_list('id'))


    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['centros_educativos'] = centro_educativo.objects.all()
        id_centro_educativo = None
        try:
            id_centro_educativo = centro_educativo.objects.filter(id=int(self.request.GET.get("id_centro_educativo"))).first()
        except:
            id_centro_educativo = None
        context['id_centro_educativo'] =  id_centro_educativo
        return context

class ListarEtapasParaInscribirAlumnos(LoginRequiredMixin, generic.ListView):
    model = Ciclo_etapa
    template_name = 'educacion/etapas_list_para_inscribir_alumnos.html'
    context_object_name = 'obj'
    login_url = 'app:login'
    queryset = Ciclo_etapa.objects.order_by('c_etapa')

    def get_queryset(self):
        existe_ciclo = Ciclo.objects.filter(estado_ciclo=True, anio = datetime.now().year).first()
        if existe_ciclo:
            return Ciclo_etapa.objects.filter(estado_ce=True, ciclo_c=existe_ciclo).order_by('c_etapa')
        return None

    def get_object(self):
        id_centro_educativo = self.kwargs.get('id_centro_educativo')
        if id_centro_educativo:
            return centro_educativo.objects.filter(id=int(id_centro_educativo)).first()
        return None

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        context['id_centro_educativo'] =  self.get_object()
        return context

class EtapasInscribirAlumnos(LoginRequiredMixin, generic.CreateView):
    model = Inscripcion_etapa
    template_name = 'educacion/Inscripcion_por_etapa.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_centro_educativo(self):
        id_centro_educativo = self.kwargs.get('id_centro_educativo')
        if id_centro_educativo:
            return centro_educativo.objects.filter(id=int(id_centro_educativo)).first()
        return None

    def get_etapa(self):
        id_etapa = self.kwargs.get('id_etapa')
        if id_etapa:
            return Ciclo_etapa.objects.filter(id=int(id_etapa)).first()
        return None

    def get(self, request, *args, **kwargs):
        id_centro = self.get_centro_educativo()
        id_etapa = self.get_etapa()
        context={}
        context['id_centro_educativo'] =  id_centro
        context['id_etapa'] = id_etapa
        context['alumnos'] = Alumno.objects.filter(estado_alumno=True).exclude(insc_alumn_etapa__centro_educ_etapa_id = id_centro.id, insc_alumn_etapa__ciclo_etapa_id = id_etapa.id)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        id_centro = self.get_centro_educativo()
        id_etapa = self.get_etapa()
        alumnos = self.request.POST.get('alumnos')
        if alumnos:
            Inscripcion_etapa.objects.create(centro_educ_etapa=id_centro, ciclo_etapa=id_etapa, alumno_etapa_id=int(alumnos))
            return redirect('educacion:etapas_list_para_inscribir_alumnos', id_centro_educativo=id_centro.id)

class InsEtapaDel(LoginRequiredMixin, generic.DeleteView):
    model = Inscripcion_etapa
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:alumno_list_para_etapas")
