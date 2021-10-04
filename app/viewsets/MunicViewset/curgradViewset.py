from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import CargoGrupo
from app.forms import CarGForm

class CarGView(LoginRequiredMixin, generic.ListView):
    model = CargoGrupo
    template_name = 'municipalizacion/carg_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class CarGNew(LoginRequiredMixin, generic.CreateView):
    model = CargoGrupo
    template_name = 'municipalizacion/carg_form.html'
    context_object_name = "obj"
    form_class = CarGForm
    success_url = reverse_lazy("municipalizacion:carg_list")
    login_url = 'app:login'

class CarGEdit(LoginRequiredMixin, generic.UpdateView):
    model = CargoGrupo
    template_name = "municipalizacion/carg_form.html"
    context_object_name = "obj"
    form_class = CarGForm
    success_url = reverse_lazy("municipalizacion:carg_list")
    login_url = 'app:login'

class CarGDel(LoginRequiredMixin, generic.DeleteView):
    model = CargoGrupo
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:carg_list")
