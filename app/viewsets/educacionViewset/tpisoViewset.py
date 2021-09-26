from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Tipo_piso
from app.forms import TpisoForm

class TpisoView(LoginRequiredMixin, generic.ListView):
    model = Tipo_piso
    template_name = 'educacion/tpiso_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class TpisoNew(LoginRequiredMixin, generic.CreateView):
    model = Tipo_piso
    template_name = "educacion/tpiso_form.html"
    context_object_name = "obj"
    form_class = TpisoForm
    success_url = reverse_lazy("educacion:tpiso_list")
    login_url = 'app:login'

class TpisoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Tipo_piso
    template_name = "educacion/tpiso_form.html"
    context_object_name = "obj"
    form_class = TpisoForm
    success_url = reverse_lazy("educacion:tpiso_list")
    login_url = 'app:login'

class TpisoDel(LoginRequiredMixin, generic.DeleteView):
    model = Tipo_piso
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:tpiso_list")
