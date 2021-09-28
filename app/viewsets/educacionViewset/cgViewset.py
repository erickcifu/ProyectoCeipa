from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Ciclo_grado
from app.forms import CGForm

class CGView(LoginRequiredMixin, generic.ListView):
    pass
    model = Ciclo_grado
    template_name = 'educacion/cg_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class CGNew(LoginRequiredMixin, generic.CreateView):
    pass
    model = Ciclo_grado
    template_name = 'educacion/cg_form.html'
    context_object_name = "obj"
    form_class = CGForm
    success_url = reverse_lazy("educacion:cg_list")
    login_url = 'app:login'

class CGEdit(LoginRequiredMixin, generic.UpdateView):
    pass
    model = Ciclo_grado
    template_name = "educacion/cg_form.html"
    context_object_name = "obj"
    form_class = CGForm
    success_url = reverse_lazy("educacion:cg_list")
    login_url = 'app:login'

class CGDel(LoginRequiredMixin, generic.DeleteView):
    pass
    model = Ciclo_grado
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:cg_list")
