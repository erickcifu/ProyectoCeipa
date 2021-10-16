from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Conviviente, Parentesco, vivienda
from app.forms import ConvivienteForm

class ConvivienteView(LoginRequiredMixin, generic.ListView):
    model = Conviviente
    template_name = 'educacion/conviviente_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ConvivienteNew(LoginRequiredMixin, generic.CreateView):
    model = Conviviente
    template_name = 'educacion/conviviente_form.html'
    context_object_name = "obj"
    form_class = ConvivienteForm
    success_url = reverse_lazy("educacion:conviviente_list")
    login_url = 'app:login'

class ConvivienteEdit(LoginRequiredMixin, generic.UpdateView):
    model = Conviviente
    template_name = "educacion/conviviente_form.html"
    context_object_name = "obj"
    form_class = ConvivienteForm
    success_url = reverse_lazy("educacion:conviviente_list")
    login_url = 'app:login'

class ConvivienteDel(LoginRequiredMixin, generic.DeleteView):
    model = Conviviente
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:conviviente_list")