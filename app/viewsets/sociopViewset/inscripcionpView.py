from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo

from app.models import InscripcionPersona, Taller, PersonaBasica
from app.forms import InscripcionpForm

class AsignarTallerPersona(LoginRequiredMixin, generic.CreateView):
    model = InscripcionPersona
    template_name = "socioproductivo/inscripcion_form.html"
    context_object_name = "obj"
    form_class = InscripcionPersona
    success_url = reverse_lazy("socioproductivo:listado_alumnos_por_taller")
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
                return ["equipoSocioproductivo/inscripcion_form.html"]
            else:
                return [self.template_name]
    
    def form_valid(self, form):
        form.save()
        if self.request.user.user_profile.rol.id == 12:
            return redirect('socioproductivo:home_equipo_socioproductivo')
        return redirect("socioproductivo:listado_alumnos_por_taller")
