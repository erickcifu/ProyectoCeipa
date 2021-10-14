from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import departamento
from app.forms import DepartamentoForm

class DeptoView(LoginRequiredMixin, generic.ListView):
    model = departamento
    template_name = 'municipalizacion/depto_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class DeptoNew(LoginRequiredMixin, generic.CreateView):
    model = departamento
    template_name = "municipalizacion/depto_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_url = reverse_lazy("municipalizacion:depto_list")
    login_url = 'app:login'

class DeptoEdit(LoginRequiredMixin, generic.UpdateView):
    model = departamento
    template_name = "municipalizacion/depto_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_url = reverse_lazy("municipalizacion:depto_list")
    login_url = 'app:login'

class DeptoDel(LoginRequiredMixin, generic.DeleteView):
    model = departamento
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:depto_list")
