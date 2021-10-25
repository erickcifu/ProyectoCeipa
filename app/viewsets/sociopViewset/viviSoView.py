from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import ViviendaSocio
from app.forms import ViviendaSForm

class ViviendSoView(LoginRequiredMixin, generic.ListView):
    model = ViviendaSocio
    template_name = 'socioproductivo/viviendSo_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ViviendSoNew(LoginRequiredMixin, generic.CreateView):
    model = ViviendaSocio
    template_name = "socioproductivo/viviendSo_form.html"
    context_object_name = "obj"
    form_class = ViviendaSForm
    success_url = reverse_lazy("socioproductivo:viviendSo_list")
    login_url = 'app:login'

class ViviendSoEdit(LoginRequiredMixin, generic.UpdateView):
    model = ViviendaSocio
    template_name = "socioproductivo/viviendSo_form.html"
    context_object_name = "obj"
    form_class = ViviendaSForm
    success_url = reverse_lazy("socioproductivo:viviendSo_list")
    login_url = 'app:login'

class ViviendSoDel(LoginRequiredMixin, generic.DeleteView):
    model = ViviendaSocio
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:viviendSo_list")
