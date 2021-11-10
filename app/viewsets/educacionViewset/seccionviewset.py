from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.models import seccion
from app.forms import SeccionForm
from app.viewsets.users.mixins.CooEduacionDirectorCentro import RolesCooEducacionDirectorCentroMixin

class SeccionView(RolesCooEducacionDirectorCentroMixin, generic.ListView):
    model = seccion
    template_name = 'educacion/seccion_list.html'
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
                return ["directorCentro/seccion_list.html"]
            else:
                return [self.template_name]

class SeccionNew(RolesCooEducacionDirectorCentroMixin, generic.CreateView):
    model = seccion
    template_name = "educacion/seccion_form.html"
    context_object_name = "obj"
    form_class = SeccionForm
    success_url = reverse_lazy("educacion:seccion_list")
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
                return ["directorCentro/seccion_form.html"]
            else:
                return [self.template_name]

class SeccionEdit(LoginRequiredMixin, generic.UpdateView):
    model = seccion
    template_name = "educacion/seccion_form.html"
    context_object_name = "obj"
    form_class = SeccionForm
    success_url = reverse_lazy("educacion:seccion_list")
    login_url = 'app:login'

class SeccionDel(LoginRequiredMixin, generic.DeleteView):
    model = seccion
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:seccion_list")
