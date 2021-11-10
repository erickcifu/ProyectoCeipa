from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.mixins.CooEduacionDirectorCentro import RolesCooEducacionDirectorCentroMixin
from app.models import Curso
from app.forms import CursoForm

class CursoView(RolesCooEducacionDirectorCentroMixin, generic.ListView):
    pass
    model = Curso
    template_name = 'educacion/curso_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'
    oaginate_by = 10

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
                    return ["directorCentro/curso_list.html"]
                else:
                    return [self.template_name]

class CursoNew(RolesCooEducacionDirectorCentroMixin, generic.CreateView):
    pass
    model = Curso
    template_name = 'educacion/curso_form.html'
    context_object_name = "obj"
    form_class = CursoForm
    success_url = reverse_lazy("educacion:curso_list")
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
                    return ["directorCentro/curso_form.html"]
                else:
                    return [self.template_name]

class CursoEdit(LoginRequiredMixin, generic.UpdateView):
    pass
    model = Curso
    template_name = "educacion/curso_form.html"
    context_object_name = "obj"
    form_class = CursoForm
    success_url = reverse_lazy("educacion:curso_list")
    login_url = 'app:login'

class CursoDel(LoginRequiredMixin, generic.DeleteView):
    pass
    model = Curso
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:curso_list")
