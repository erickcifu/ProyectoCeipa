from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.views import generic
from django.urls import reverse_lazy

from app.models import municipio
from app.forms import MunicipioForm

class MunicipioView(LoginRequiredMixin, generic.ListView):
    model = municipio
    template_name = 'educacion/municipio_list.html'
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
                return ["CoordinadorMunicipal/municipio_list.html"]

class MunicipioNew(LoginRequiredMixin, generic.CreateView):
    model = municipio
    template_name = "educacion/municipio_form.html"
    context_object_name = "obj"
    form_class = MunicipioForm
    success_url = reverse_lazy("educacion:municipio_list")
    login_url = 'app:login'

    def get_template_names(self):
        id_rol = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if id_rol == 1 or id_rol == 2:
                return [self.template_name]
            elif id_rol == 7 or id_rol == 8:
                return ["CoordinadorMunicipal/municipio_form.html"]

class MunicipioEdit(LoginRequiredMixin, generic.UpdateView):
    model = municipio
    template_name = "educacion/municipio_form.html"
    context_object_name = "obj"
    form_class = MunicipioForm
    success_url = reverse_lazy("educacion:municipio_list")
    login_url = 'app:login'

    def get_template_names(self):
        id_rol = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if id_rol == 1 or id_rol == 2:
                return [self.template_name]
            elif id_rol == 7 or id_rol == 8:
                return ["CoordinadorMunicipal/municipio_form.html"]

class MunicipioDel(LoginRequiredMixin, generic.DeleteView):
    model = municipio
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:municipio_list")

    def get_template_names(self):
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
