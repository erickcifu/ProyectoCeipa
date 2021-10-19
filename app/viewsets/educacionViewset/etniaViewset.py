from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import etnia
from app.forms import EtniaForm

class EtniaView(LoginRequiredMixin, generic.ListView):
    model = etnia
    template_name = 'educacion/etnia_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class EtniaNew(LoginRequiredMixin, generic.CreateView):
    model = etnia
    template_name = "educacion/etnia_form.html"
    context_object_name = "obj"
    form_class = EtniaForm
    success_url = reverse_lazy("educacion:etnia_list")
    login_url = 'app:login'

class EtniaEdit(LoginRequiredMixin, generic.UpdateView):
    model = etnia
    template_name = "educacion/etnia_form.html"
    context_object_name = "obj"
    form_class = EtniaForm
    success_url = reverse_lazy("educacion:etnia_list")
    login_url = 'app:login'

class EtniaDel(LoginRequiredMixin, generic.DeleteView):
    model = etnia
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:etnia_list")