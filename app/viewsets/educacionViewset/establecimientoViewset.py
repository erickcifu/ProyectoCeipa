from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Establecimiento
from app.forms import EstablecimientoForm

class EstablecimientoView(LoginRequiredMixin, generic.ListView):
    model = Establecimiento
    template_name = 'educacion/establecimiento_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class EstablecimientoNew(LoginRequiredMixin, generic.CreateView):
    model = Establecimiento
    template_name = "educacion/establecimiento_form.html"
    context_object_name = "obj"
    form_class = EstablecimientoForm
    success_url = reverse_lazy("educacion:establecimiento_list")
    login_url = 'app:login'

class EstablecimientoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Establecimiento
    template_name = "educacion/establecimiento_form.html"
    context_object_name = "obj"
    form_class = EstablecimientoForm
    success_url = reverse_lazy("educacion:establecimiento_list")
    login_url = 'app:login'

class EstablecimientoDel(LoginRequiredMixin, generic.DeleteView):
    model = Establecimiento
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:establecimiento_list")