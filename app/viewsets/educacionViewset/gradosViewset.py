from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from app.viewsets.users.CoordinadorEducacion.mixin import IsCoordinadorEducacionMixin
from app.viewsets.users.directorCentro.mixin import IsDirectorCentroMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import grados, Ciclo, Ciclo_grado, centro_educativo
from app.forms import GradosForm

class GradosView(LoginRequiredMixin, generic.ListView):
    model = grados
    template_name = 'educacion/grados_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class GradosNew(LoginRequiredMixin, generic.CreateView):
    model = grados
    template_name = 'educacion/grados_form.html'
    context_object_name = "obj"
    form_class = GradosForm
    success_url = reverse_lazy("educacion:grados_list")
    login_url = 'app:login'

class GradosEdit(LoginRequiredMixin, generic.UpdateView):
    model = grados
    template_name = "educacion/grados_form.html"
    context_object_name = "obj"
    form_class = GradosForm
    success_url = reverse_lazy("educacion:grados_list")
    login_url = 'app:login'

class GradosDel(LoginRequiredMixin, generic.DeleteView):
    model = grados
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:grados_list")

#traer los grados del centro educativo
#ciclo_grado.objects.filter(cgc_cg__maestro__p_educativo__centro_Educativo__id=1).first()
#Ciclo_grado.objects.filter(cgc_cg__maestro__p_educativo__centro_Educativo__id__in=centro_educativo.objects.values_list('id'), ciclo__id__in=[Ciclo.objects.all().values_list('id)])

#Ciclo_grado.objects.filter(cgc_cg__maestro__p_educativo__centro_Educativo__id=1).annotate(maestro=F('cgc_cg__maestro__nombres')).first().maestro

#listar los grados por el centro educativo
class ListarGradosPorCentroEducacion(LoginRequiredMixin, generic.ListView):
    model = grados
    template_name = 'educacion/grados_por_centro_educativo.html'
    context_object_name = 'obj'

    def get_queryset(self):
        id_centro_educativo = self.request.GET.get("id_centro_educativo")
        if id_centro_educativo:
            return Ciclo_grado.objects.filter(cgc_cg__maestro__p_educativo__centro_Educativo__id=int(id_centro_educativo))

        return Ciclo_grado.objects.filter(cgc_cg__maestro__p_educativo__centro_Educativo__id__in=centro_educativo.objects.values_list('id'))

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

#rol de director
class ListarGradosDeCadaCentro(IsDirectorCentroMixin, generic.ListView):
    model = Ciclo_grado
    template_name = 'educacion/grados_por_centro_educativo.html'
    context_object_name = 'obj'

    def get_queryset(self):
        id_centro_educativo = self.kwargs.get("id_centro_educativo")
        if id_centro_educativo:
            return Ciclo_grado.objects.filter(cgc_cg__maestro__p_educativo__centro_Educativo__id=int(id_centro_educativo))
