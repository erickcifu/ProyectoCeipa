from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Emprendimiento
from app.forms import EmprenForm

class EmprenView(LoginRequiredMixin, generic.ListView):
    model = Emprendimiento
    template_name = 'socioproductivo/Emprendimiento_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class EmprenNew(LoginRequiredMixin, generic.CreateView):
    model = Emprendimiento
    template_name = "socioproductivo/Emprendimiento_form.html"
    context_object_name = "obj"
    form_class = EmprenForm
    success_url = reverse_lazy("socioproductivo:emprend_list")
    login_url = 'app:login'

class EmprenEdit(LoginRequiredMixin, generic.UpdateView):
    model = Emprendimiento
    template_name = "socioproductivo/Emprendimiento_form.html"
    context_object_name = "obj"
    form_class = EmprenForm
    success_url = reverse_lazy("socioproductivo:emprend_list")
    login_url = 'app:login'

class EmprenDel(LoginRequiredMixin, generic.DeleteView):
    model = Emprendimiento
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:emprend_list")
