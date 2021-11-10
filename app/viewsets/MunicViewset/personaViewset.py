from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Persona
from app.forms import PersonaForm
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin

class PerView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = Persona
    template_name = 'municipalizacion/persona_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PerNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = Persona
    template_name = 'municipalizacion/persona_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    success_url = reverse_lazy("municipalizacion:per_list")
    login_url = 'app:login'

    def get_template_names(self):
        user = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if user == 7 or user == 8:
                return [self.template_name]
            elif user == 9:
                return ["equipoMunicipal/persona_form.html"]
            else:
                return [self.template_name]

    def form_valid(self, form):
        form.save()
        if self.request.user.user_profile.rol.id == 9:
            return redirect('municipalizacion:home_equipo_municipal')
        return redirect("municipalizacion:per_list")

class PerEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    model = Persona
    template_name = "municipalizacion/persona_form.html"
    context_object_name = "obj"
    form_class = PersonaForm
    success_url = reverse_lazy("municipalizacion:per_list")
    login_url = 'app:login'

class PerDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = Persona
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:per_list")
