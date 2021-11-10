from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo
from app.models import GrupoNA
from app.forms import GrupoNAForm

class GrupoNAView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = GrupoNA
    template_name = 'socioproductivo/grupona_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class GrupoNANew(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.CreateView):
    model = GrupoNA
    template_name = "socioproductivo/grupona_form.html"
    context_object_name = "obj"
    form_class = GrupoNAForm
    success_url = reverse_lazy("socioproductivo:grupona_list")
    login_url = 'app:login'

    def get_template_names(self):
        user = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if user == 10 or user == 11:
                return [self.template_name]
            elif user == 12:
                return ["equipoSocioproductivo/grupona_form.html"]
            else:
                return [self.template_name]

    def form_valid(self, form):
        form.save()
        if self.request.user.user_profile.rol.id == 12:
            return redirect('socioproductivo:home_equipo_socioproductivo')
        return redirect("socioproductivo:grupona_list")

class GrupoNAEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = GrupoNA
    template_name = "socioproductivo/grupona_form.html"
    context_object_name = "obj"
    form_class = GrupoNAForm
    success_url = reverse_lazy("socioproductivo:grupona_list")
    login_url = 'app:login'

class GrupoNADel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = GrupoNA
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:grupona_list")
