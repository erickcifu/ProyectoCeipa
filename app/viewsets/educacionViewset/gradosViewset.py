from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import grados
from app.forms import GradosForm

class GradosView(LoginRequiredMixin, generic.ListView):
    model = grados
    template_name = 'educacion/grados_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class GradosNew(LoginRequiredMixin, generic.CreateView):
    model = grados
    template_name = 'educacion/grados_form.html'
    context_object_name = "obj"
    form_class = GradosForm
    success_url = reverse_lazy("educacion:grados_list")
    login_url = 'app:login'

class GradosEdit(LoginRequiredMixin, generic.UpdateView):
    model = grados
    template_name = "educacion/grados_form.html"
    context_object_name = "obj"
    form_class = GradosForm
    success_url = reverse_lazy("educacion:grados_list")
    login_url = 'app:login'

class GradosDel(LoginRequiredMixin, generic.DeleteView):
    model = grados
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:grados_list")
