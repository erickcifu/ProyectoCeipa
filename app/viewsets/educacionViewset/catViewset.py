from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Categoria
from app.forms import CategoriaForm

class CatView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = 'educacion/cat_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class CatNew(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = "educacion/cat_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("educacion:cat_list")
    login_url = 'app:login'

class CatEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = "educacion/cat_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("educacion:cat_list")
    login_url = 'app:login'

class CatDel(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:cat_list")
