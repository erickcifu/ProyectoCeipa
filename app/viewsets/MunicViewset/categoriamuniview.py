from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Categoria
from app.forms import CategoriaForm

class CatmuniView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = Categoria
    template_name = 'municipalizacion/catmuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class CatmuniNew(IsCoordinadorMunicipalMixin, generic.CreateView):
    model = Categoria
    template_name = "municipalizacion/catmuni_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("municipalizacion:catmuni_list")
    login_url = 'app:login'

class CatmuniEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    model = Categoria
    template_name = "municipalizacion/catmuni_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("municipalizacion:catmuni_list")
    login_url = 'app:login'

class CatmuniDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = Categoria
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:catmuni_list")
