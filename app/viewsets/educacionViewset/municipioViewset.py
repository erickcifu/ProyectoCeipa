from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import municipio
from app.forms import MunicipioForm

class MunicipioView(LoginRequiredMixin, generic.ListView):
    model = municipio
    template_name = 'educacion/municipio_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class MunicipioNew(LoginRequiredMixin, generic.CreateView):
    model = municipio
    template_name = "educacion/municipio_form.html"
    context_object_name = "obj"
    form_class = MunicipioForm
    success_url = reverse_lazy("educacion:municipio_list")
    login_url = 'app:login'

class MunicipioEdit(LoginRequiredMixin, generic.UpdateView):
    model = municipio
    template_name = "educacion/municipio_form.html"
    context_object_name = "obj"
    form_class = MunicipioForm
    success_url = reverse_lazy("educacion:municipio_list")
    login_url = 'app:login'

class MunicipioDel(LoginRequiredMixin, generic.DeleteView):
    model = municipio
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:municipio_list")
