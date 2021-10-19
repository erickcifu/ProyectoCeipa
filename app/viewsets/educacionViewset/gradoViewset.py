from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Grado
from app.forms import GradoForm

class GradoView(LoginRequiredMixin, generic.ListView):
    model = Grado
    template_name = 'educacion/grado_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class GradoNew(LoginRequiredMixin, generic.CreateView):
    model = Grado
    template_name = "educacion/grado_form.html"
    context_object_name = "obj"
    form_class = GradoForm
    success_url = reverse_lazy("educacion:grado_list")
    login_url = 'app:login'

class GradoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Grado
    template_name = "educacion/grado_form.html"
    context_object_name = "obj"
    form_class = GradoForm
    success_url = reverse_lazy("educacion:grado_list")
    login_url = 'app:login'

class GradoDel(LoginRequiredMixin, generic.DeleteView):
    model = Grado
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:grado_list")