from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import genero
from app.forms import GeneroForm

class GeneroMuniView(LoginRequiredMixin, generic.ListView):
    model = genero
    template_name = 'municipalizacion/generomuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class GeneroMuniNew(LoginRequiredMixin, generic.CreateView):
    model = genero
    template_name = 'municipalizacion/generomuni_form.html'
    context_object_name = "obj"
    form_class = GeneroForm
    success_url = reverse_lazy("municipalizacion:generomuni_list")
    login_url = 'app:login'

class GeneroMuniEdit(LoginRequiredMixin, generic.UpdateView):
    model = genero
    template_name = "municipalizacion/generomuni_form.html"
    context_object_name = "obj"
    form_class = GeneroForm
    success_url = reverse_lazy("municipalizacion:generomuni_list")
    login_url = 'app:login'

class GeneroMuniDel(LoginRequiredMixin, generic.DeleteView):
    model = genero
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:generomuni_list")
