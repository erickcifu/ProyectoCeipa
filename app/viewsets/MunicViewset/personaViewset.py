from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Persona
from app.forms import PersonaForm

class PerView(LoginRequiredMixin, generic.ListView):
    model = Persona
    template_name = 'municipalizacion/persona_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PerNew(LoginRequiredMixin, generic.CreateView):
    model = Persona
    template_name = 'municipalizacion/persona_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    success_url = reverse_lazy("municipalizacion:per_list")
    login_url = 'app:login'

class PerEdit(LoginRequiredMixin, generic.UpdateView):
    model = Persona
    template_name = "municipalizacion/persona_form.html"
    context_object_name = "obj"
    form_class = PersonaForm
    success_url = reverse_lazy("municipalizacion:per_list")
    login_url = 'app:login'

class PerDel(LoginRequiredMixin, generic.DeleteView):
    model = Persona
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:per_list")
