from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import genero
from app.forms import GeneroForm

class GeneroView(LoginRequiredMixin, generic.ListView):
    model = genero
    template_name = 'educacion/genero_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class GeneroNew(LoginRequiredMixin, generic.CreateView):
    model = genero
    template_name = 'educacion/genero_form.html'
    context_object_name = "obj"
    form_class = GeneroForm
    success_url = reverse_lazy("educacion:genero_list")
    login_url = 'app:login'

class GeneroEdit(LoginRequiredMixin, generic.UpdateView):
    model = genero
    template_name = "educacion/genero_form.html"
    context_object_name = "obj"
    form_class = GeneroForm
    success_url = reverse_lazy("educacion:genero_list")
    login_url = 'app:login'

class GeneroDel(LoginRequiredMixin, generic.DeleteView):
    model = genero
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:genero_list")
