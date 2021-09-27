from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Religion_alumno
from app.forms import ReligionAlumnoForm

class Religion_alumnoView(LoginRequiredMixin, generic.ListView):
    model = Religion_alumno
    template_name = 'educacion/religionalum_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class Religion_alumnoNew(LoginRequiredMixin, generic.CreateView):
    model = Religion_alumno
    template_name = "educacion/religionalum_form.html"
    context_object_name = "obj"
    form_class = ReligionAlumnoForm
    success_url = reverse_lazy("educacion:religionalum_list")
    login_url = 'app:login'

class Religion_alumnoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Religion_alumno
    template_name = "educacion/religionalum_form.html"
    context_object_name = "obj"
    form_class = ReligionAlumnoForm
    success_url = reverse_lazy("educacion:religionalum_list")
    login_url = 'app:login'

class Religion_alumnoDel(LoginRequiredMixin, generic.DeleteView):
    model = Religion_alumno
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:religionalum_list")