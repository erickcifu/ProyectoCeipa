from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.views import generic
from django.urls import reverse_lazy

from app.models import departamento
from app.forms import DepartamentoForm

class DepartamentoView(LoginRequiredMixin, generic.ListView):
    model = departamento
    template_name = 'educacion/departamento_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_template_names(self):
        """
        Return a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response() is overridden.
        """
        id_rol = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if id_rol == 1 or id_rol == 2:
                return [self.template_name]
            elif id_rol == 7 or id_rol == 8:
                return ["CoordinadorMunicipal/departamento_list.html"]


class DepartamentoNew(LoginRequiredMixin, generic.CreateView):
    model = departamento
    template_name = "educacion/departamento_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_url = reverse_lazy("educacion:departamento_list")
    login_url = 'app:login'

    def get_template_names(self):
        """
        Return a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response() is overridden.
        """
        id_rol = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if id_rol == 1 or id_rol == 2:
                return [self.template_name]
            elif id_rol == 7 or id_rol == 8:
                return ["CoordinadorMunicipal/departamento_form.html"]

class DepartamentoEdit(LoginRequiredMixin, generic.UpdateView):
    model = departamento
    template_name = "educacion/departamento_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_url = reverse_lazy("educacion:departamento_list")
    login_url = 'app:login'

    def get_template_names(self):
        """
        Return a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response() is overridden.
        """
        id_rol = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if id_rol == 1 or id_rol == 2:
                return [self.template_name]
            elif id_rol == 7 or id_rol == 8:
                return ["CoordinadorMunicipal/departamento_form.html"]

class DepartamentoDel(LoginRequiredMixin, generic.DeleteView):
    model = departamento
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:departamento_list")

    def get_template_names(self):
        """
        Return a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response() is overridden.
        """
        id_rol = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if id_rol == 1 or id_rol == 2:
                return [self.template_name]
            elif id_rol == 7 or id_rol == 8:
                return ["CoordinadorMunicipal/catalogos_del.html"]
