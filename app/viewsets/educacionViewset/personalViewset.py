from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from app.viewsets.users.CoordinadorEducacion.mixin import IsCoordinadorEducacionMixin
from app.viewsets.users.directorCentro.mixin import IsDirectorCentroMixin

from app.models import personalEducativo, centro_educativo
from app.forms import PersonalForm, MaestroCentroForm, DirectorCentroForm

class PersonalView(IsCoordinadorEducacionMixin, generic.ListView):
    model = personalEducativo
    template_name = 'educacion/personal_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PersonalNew(IsCoordinadorEducacionMixin, generic.CreateView):
    model = personalEducativo
    template_name = 'educacion/personal_form.html'
    context_object_name = "obj"
    form_class = PersonalForm
    success_url = reverse_lazy("educacion:listado_personal_por_centro_educativo")
    login_url = 'app:login'

class PersonalMaestroNew(IsCoordinadorEducacionMixin, generic.CreateView):
    model = personalEducativo
    template_name = 'educacion/personal_maestro_form.html'
    context_object_name = "obj"
    form_class = MaestroCentroForm
    success_url = reverse_lazy("educacion:listado_personal_por_centro_educativo")
    login_url = 'app:login'

class PersonalDirectorCentroNew(IsCoordinadorEducacionMixin, generic.CreateView):
    model = personalEducativo
    template_name = 'educacion/personal_director_form.html'
    context_object_name = "obj"
    form_class = DirectorCentroForm
    success_url = reverse_lazy("educacion:listar_maestro_director_centro")
    login_url = 'app:login'

class PersonalEdit(IsCoordinadorEducacionMixin, generic.UpdateView):
    model = personalEducativo
    template_name = "educacion/personal_form.html"
    context_object_name = "obj"
    form_class = PersonalForm
    success_url = reverse_lazy("educacion:personal_list")
    login_url = 'app:login'

class PersonalDel(IsCoordinadorEducacionMixin, generic.DeleteView):
    model = personalEducativo
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:personal_list")

#listando los maestros por centro educativo
class ListarPersonalEducativoPorCentroEducativo(IsCoordinadorEducacionMixin, generic.ListView):
    model = personalEducativo
    template_name = 'educacion/personal_listar_por_centro_educativo.html'
    context_object_name = 'obj'

    def get_queryset(self):
        id_centro_educativo = self.request.GET.get("id_centro_educativo")
        if id_centro_educativo:
            return personalEducativo.objects.filter(p_educativo__centro_Educativo_id=int(id_centro_educativo))

        return personalEducativo.objects.filter(p_educativo__centro_Educativo_id__in=centro_educativo.objects.filter(estado_centro=True).values_list('id'))


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

#rol director
class ListarPersonalEnCadaCentro(IsDirectorCentroMixin, generic.ListView):
    model = personalEducativo
    template_name = 'directorCentro/personalDeCadaCentro.html'
    context_object_name = 'obj'

    def get_object(self):
        user = self.request.user
        return centro_educativo.objects.filter(c_educativo__personal__perfile = user.user_profile).first()

    def get_queryset(self):
        centro = self.get_object()
        if centro:
            return personalEducativo.objects.filter(p_educativo__centro_Educativo_id=int(centro.id))

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['id_centro_educativo'] =  self.get_object()
        return context
