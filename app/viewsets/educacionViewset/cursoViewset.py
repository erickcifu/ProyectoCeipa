from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Curso
from app.forms import CursoForm

class CursoView(LoginRequiredMixin, generic.ListView):
    pass
    model = Curso
    template_name = 'educacion/curso_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class CursoNew(LoginRequiredMixin, generic.CreateView):
    pass
    model = Curso
    template_name = 'educacion/curso_form.html'
    context_object_name = "obj"
    form_class = CursoForm
    success_url = reverse_lazy("educacion:curso_list")
    login_url = 'app:login'

class CursoEdit(LoginRequiredMixin, generic.UpdateView):
    pass
    model = Curso
    template_name = "educacion/curso_form.html"
    context_object_name = "obj"
    form_class = Curso
    success_url = reverse_lazy("educacion:curso_list")
    login_url = 'app:login'

class CursoDel(LoginRequiredMixin, generic.DeleteView):
    pass
    model = Curso
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:curso_list")
