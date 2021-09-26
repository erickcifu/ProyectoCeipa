from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Apadecimiento
from app.forms import APadeForm

class APadView(LoginRequiredMixin, generic.ListView):
    model = Apadecimiento
    template_name = 'educacion/apad_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class APadNew(LoginRequiredMixin, generic.CreateView):
    model = Apadecimiento
    template_name = "educacion/apad_form.html"
    context_object_name = "obj"
    form_class = APadeForm
    success_url = reverse_lazy("educacion:apad_list")
    login_url = 'app:login'

class APadEdit(LoginRequiredMixin, generic.UpdateView):
    model = Apadecimiento
    template_name = "educacion/pade_form.html"
    context_object_name = "obj"
    form_class = APadeForm
    success_url = reverse_lazy("educacion:apad_list")
    login_url = 'app:login'

class APadDel(LoginRequiredMixin, generic.DeleteView):
    model = Apadecimiento
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:apad_list")
