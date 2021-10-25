from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Encargado
from app.forms import EncargadoForm

class EncargadoView(LoginRequiredMixin, generic.ListView):
    model = Encargado
    template_name = 'socioproductivo/Encargado_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class EncargadoNew(LoginRequiredMixin, generic.CreateView):
    model = Encargado
    template_name = "socioproductivo/Encargado_form.html"
    context_object_name = "obj"
    form_class = EncargadoForm
    success_url = reverse_lazy("socioproductivo:Encar_list")
    login_url = 'app:login'

class EncargadoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Encargado
    template_name = "socioproductivo/Encargado_form.html"
    context_object_name = "obj"
    form_class = EncargadoForm
    success_url = reverse_lazy("socioproductivo:Encar_list")
    login_url = 'app:login'

class EncargadoDel(LoginRequiredMixin, generic.DeleteView):
    model = Encargado
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:Encar_list")
