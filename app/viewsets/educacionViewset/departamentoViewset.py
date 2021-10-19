from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import departamento
from app.forms import DepartamentoForm

class DepartamentoView(LoginRequiredMixin, generic.ListView):
    model = departamento
    template_name = 'educacion/departamento_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class DepartamentoNew(LoginRequiredMixin, generic.CreateView):
    model = departamento
    template_name = "educacion/departamento_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_url = reverse_lazy("educacion:departamento_list")
    login_url = 'app:login'

class DepartamentoEdit(LoginRequiredMixin, generic.UpdateView):
    model = departamento
    template_name = "educacion/departamento_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_url = reverse_lazy("educacion:departamento_list")
    login_url = 'app:login'

class DepartamentoDel(LoginRequiredMixin, generic.DeleteView):
    model = departamento
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:departamento_list")
