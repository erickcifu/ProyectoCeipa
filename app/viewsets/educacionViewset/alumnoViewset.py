from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Alumno
from app.forms import AlumnoForm

class AlumnoView(LoginRequiredMixin, generic.ListView):
    model = Alumno
    template_name = 'educacion/alumno_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class AlumnoNew(LoginRequiredMixin, generic.CreateView):
    model = Alumno
    template_name = 'educacion/alumno_form.html'
    context_object_name = "obj"
    form_class = AlumnoForm
    success_url = reverse_lazy("educacion:alumno_list")
    login_url = 'app:login'

class AlumnoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Alumno
    template_name = "educacion/alumno_form.html"
    context_object_name = "obj"
    form_class = AlumnoForm
    success_url = reverse_lazy("educacion:alumno_list")
    login_url = 'app:login'

class AlumnoDel(LoginRequiredMixin, generic.DeleteView):
    model = Alumno
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:alumno_list")