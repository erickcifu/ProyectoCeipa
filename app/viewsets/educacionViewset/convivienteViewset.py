from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.forms.educacionForms.convivienteForm import ConvivienteFormEdit

from app.models import Conviviente, Parentesco, vivienda
from app.forms import ConvivienteForm

class ConvivienteView(LoginRequiredMixin, generic.ListView):
    model = Conviviente
    template_name = 'educacion/conviviente_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ConvivienteNew(LoginRequiredMixin, generic.CreateView):
    model = Conviviente
    template_name = 'educacion/conviviente_form.html'
    context_object_name = "obj"
    form_class = ConvivienteForm
    success_url = reverse_lazy("educacion:conviviente_list")
    login_url = 'app:login'

class ConvivienteEdit(LoginRequiredMixin, generic.UpdateView):
    model = Conviviente
    template_name = "educacion/conviviente_form.html"
    context_object_name = "obj"
    form_class = ConvivienteForm
    success_url = reverse_lazy("educacion:conviviente_list")
    login_url = 'app:login'

class ConvivienteDel(LoginRequiredMixin, generic.DeleteView):
    model = Conviviente
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:conviviente_list")

class ConvivienteAlumnoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Conviviente
    template_name = "educacion/conviviente_form.html"
    context_object_name = "obj"
    form_class = ConvivienteForm
    success_url = reverse_lazy("educacion:conviviente_list")
    login_url = 'app:login'

    def get_template_names(self):
            if self.template_name is None:
                raise ImproperlyConfigured(
                    "TemplateResponseMixin requires either a definition of "
                    "'template_name' or an implementation of 'get_template_names()'")
            else:
                if self.request.user.user_profile.rol.id == 1 or self.request.user.user_profile.rol.id == 2:
                    return [self.template_name]
                elif self.request.user.user_profile.rol.id == 5:
                    return ["directorCentro/conviviente_form.html"]

    def form_valid(self, form):
        form.save()
        return redirect('educacion:alumno_list_convivientes', pk=self.get_object().vivienda.estudiante.id)
