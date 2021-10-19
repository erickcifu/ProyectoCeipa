from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import personalEducativo, centro_educativo
from app.forms import PersonalForm

class PersonalView(LoginRequiredMixin, generic.ListView):
    model = personalEducativo
    template_name = 'educacion/personal_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PersonalNew(LoginRequiredMixin, generic.CreateView):
    model = personalEducativo
    template_name = 'educacion/personal_form.html'
    context_object_name = "obj"
    form_class = PersonalForm
    success_url = reverse_lazy("educacion:listado_personal_por_centro_educativo")
    login_url = 'app:login'

class PersonalEdit(LoginRequiredMixin, generic.UpdateView):
    model = personalEducativo
    template_name = "educacion/personal_form.html"
    context_object_name = "obj"
    form_class = PersonalForm
    success_url = reverse_lazy("educacion:personal_list")
    login_url = 'app:login'

class PersonalDel(LoginRequiredMixin, generic.DeleteView):
    model = personalEducativo
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:personal_list")

#listando los maestros por centro educativo
class ListarPersonalEducativoPorCentroEducativo(LoginRequiredMixin, generic.ListView):
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

    