from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import idioma
from app.forms import IdiomaForm

class IdiomaView(LoginRequiredMixin, generic.ListView):
    model = idioma
    template_name = 'educacion/idioma_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class IdiomaNew(LoginRequiredMixin, generic.CreateView):
    model = idioma
    template_name = 'educacion/idioma_form.html'
    context_object_name = "obj"
    form_class = IdiomaForm
    success_url = reverse_lazy("educacion:idioma_list")
    login_url = 'app:login'

class IdiomaEdit(LoginRequiredMixin, generic.UpdateView):
    model = idioma
    template_name = "educacion/idioma_form.html"
    context_object_name = "obj"
    form_class = IdiomaForm
    success_url = reverse_lazy("educacion:idioma_list")
    login_url = 'app:login'

class IdiomaDel(LoginRequiredMixin, generic.DeleteView):
    model = idioma
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:idioma_list")
