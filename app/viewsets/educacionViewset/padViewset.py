from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Padecimiento
from app.forms import PadeForm

class PadView(LoginRequiredMixin, generic.ListView):
    model = Padecimiento
    template_name = 'educacion/pade_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PadNew(LoginRequiredMixin, generic.CreateView):
    model = Padecimiento
    template_name = "educacion/pade_form.html"
    context_object_name = "obj"
    form_class = PadeForm
    success_url = reverse_lazy("educacion:pade_list")
    login_url = 'app:login'

class PadEdit(LoginRequiredMixin, generic.UpdateView):
    model = Padecimiento
    template_name = "educacion/pade_form.html"
    context_object_name = "obj"
    form_class = PadeForm
    success_url = reverse_lazy("educacion:pade_list")
    login_url = 'app:login'

class PadDel(LoginRequiredMixin, generic.DeleteView):
    model = Padecimiento
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:pade_list")
