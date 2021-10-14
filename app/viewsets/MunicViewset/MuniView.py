from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import municipio
from app.forms import MunicipioForm

class MunicView(LoginRequiredMixin, generic.ListView):
    model = municipio
    template_name = 'municipalizacion/muni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class MuniNew(LoginRequiredMixin, generic.CreateView):
    model = municipio
    template_name = "municipalizacion/muni_form.html"
    context_object_name = "obj"
    form_class = MunicipioForm
    success_url = reverse_lazy("municipalizacion:muni_list")
    login_url = 'app:login'

class MuniEdit(LoginRequiredMixin, generic.UpdateView):
    model = municipio
    template_name = "municipalizacion/muni_form.html"
    context_object_name = "obj"
    form_class = MunicipioForm
    success_url = reverse_lazy("municipalizacion:muni_list")
    login_url = 'app:login'

class MuniDel(LoginRequiredMixin, generic.DeleteView):
    model = municipio
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:muni_list")
