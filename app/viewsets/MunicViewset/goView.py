from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import GOrganizado
from app.forms import GOrgForm

class GrupoOrganizadoView(LoginRequiredMixin, generic.ListView):
    model = GOrganizado
    template_name = 'municipalizacion/Go_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class GrupoOrganizadoNew(LoginRequiredMixin, generic.CreateView):
    model = GOrganizado
    template_name = "municipalizacion/Go_form.html"
    context_object_name = "obj"
    form_class = GOrgForm
    success_url = reverse_lazy("municipalizacion:Gorg_list")
    login_url = 'app:login'

class GrupoOrganizadoEdit(LoginRequiredMixin, generic.UpdateView):
    model = GOrganizado
    template_name = "municipalizacion/Go_form.html"
    context_object_name = "obj"
    form_class = GOrgForm
    success_url = reverse_lazy("municipalizacion:Gorg_list")
    login_url = 'app:login'

class GrupoOrganizadoDel(LoginRequiredMixin, generic.DeleteView):
    model = GOrganizado
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:Gorg_list")
