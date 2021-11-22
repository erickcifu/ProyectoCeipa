from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo
from app.models import Taller
from app.forms import TallerForm

class TallerView(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.ListView):
    model = Taller
    template_name = 'socioproductivo/talleres_list.html'
    context_object_name = 'obj'
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
                return ["equipoSocioproductivo/talleres_list.html"]
            
class TallerNew(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.CreateView):
    model = Taller
    template_name = "socioproductivo/talleres_form.html"
    context_object_name = "obj"
    form_class = TallerForm
    success_url = reverse_lazy("socioproductivo:talleres_list")
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
                return ["equipoSocioproductivo/talleres_form.html"]
            else:
                return [self.template_name]

    def form_valid(self, form):
        form.save()
        if self.request.user.user_profile.rol.id == 12:
            return redirect('socioproductivo:home_equipo_socioproductivo')
        return redirect("socioproductivo:talleres_list")


class TallerEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = Taller
    template_name = "socioproductivo/talleres_form.html"
    context_object_name = "obj"
    form_class = TallerForm
    success_url = reverse_lazy("socioproductivo:talleres_list")
    login_url = 'app:login'

class TallerDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = Taller
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:talleres_list")
