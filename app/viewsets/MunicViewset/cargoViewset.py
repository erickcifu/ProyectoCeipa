from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Cargo
from app.forms import CargoForm

class CarView(LoginRequiredMixin, generic.ListView):
    model = Cargo
    template_name = 'municipalizacion/cargo_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class CarNew(LoginRequiredMixin, generic.CreateView):
    model = Cargo
    template_name = 'municipalizacion/cargo_form.html'
    context_object_name = "obj"
    form_class = CargoForm
    success_url = reverse_lazy("municipalizacion:cargo_list")
    login_url = 'app:login'

class CarEdit(LoginRequiredMixin, generic.UpdateView):
    model = Cargo
    template_name = "municipalizacion/cargo_form.html"
    context_object_name = "obj"
    form_class = CargoForm
    success_url = reverse_lazy("municipalizacion:cargo_list")
    login_url = 'app:login'

class CarDel(LoginRequiredMixin, generic.DeleteView):
    model = Cargo
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:cargo_list")
