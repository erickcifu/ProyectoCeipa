from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo

from app.models import JornadaEstudios
from app.forms import JornadaesForm

class JornadaEsView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = JornadaEstudios
    template_name = 'socioproductivo/jornadaes_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class JornadaEsNew(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.CreateView):
    model = JornadaEstudios
    template_name = "socioproductivo/jornadaes_form.html"
    context_object_name = "obj"
    form_class = JornadaesForm
    success_url = reverse_lazy("socioproductivo:jornadaes_list")
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
                return ["equipoSocioproductivo/jornadaes_form.html"]
            else:
                return [self.template_name]

    def form_valid(self, form):
        form.save()
        if self.request.user.user_profile.rol.id == 12:
            return redirect('socioproductivo:home_equipo_socioproductivo')
        return redirect("socioproductivo:jornadaes_list")

class JornadaEsEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = JornadaEstudios
    template_name = "socioproductivo/jornadaes_form.html"
    context_object_name = "obj"
    form_class = JornadaesForm
    success_url = reverse_lazy("socioproductivo:jornadaes_list")
    login_url = 'app:login'

class JornadaEsDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = JornadaEstudios
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:jornadaes_list")
