from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.mixins.CooEduacionDirectorCentro import RolesCooEducacionDirectorCentroMixin

from app.models import Grado
from app.forms import GradoForm

class GradoView(LoginRequiredMixin, generic.ListView):
    model = Grado
    template_name = 'educacion/grado_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_template_names(self):
        user = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if user == 1 or user == 2:
                return [self.template_name]
            elif user == 5:
                return ["directorCentro/grado_list.html"]
            else:
                return [self.template_name]

class GradoNew(LoginRequiredMixin, generic.CreateView):
    model = Grado
    template_name = "educacion/grado_form.html"
    context_object_name = "obj"
    form_class = GradoForm
    success_url = reverse_lazy("educacion:grado_list")
    login_url = 'app:login'

    def get_template_names(self):
        user = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if user == 1 or user == 2:
                return [self.template_name]
            elif user == 5:
                return ["directorCentro/grado_form.html"]
            else:
                return [self.template_name]

class GradoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Grado
    template_name = "educacion/grado_form.html"
    context_object_name = "obj"
    form_class = GradoForm
    success_url = reverse_lazy("educacion:grado_list")
    login_url = 'app:login'

class GradoDel(LoginRequiredMixin, generic.DeleteView):
    model = Grado
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:grado_list")
