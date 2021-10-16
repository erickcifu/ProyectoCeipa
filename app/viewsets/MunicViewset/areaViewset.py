from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Area
from app.forms import AreaForm

class AreaView(LoginRequiredMixin, generic.ListView):
    model = Area
    template_name = 'municipalizacion/area_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class AreaNew(LoginRequiredMixin, generic.CreateView):
    model = Area
    template_name = 'municipalizacion/area_form.html'
    context_object_name = "obj"
    form_class = AreaForm
    success_url = reverse_lazy("municipalizacion:area_list")
    login_url = 'app:login'

class AreaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Area
    template_name = "municipalizacion/area_form.html"
    context_object_name = "obj"
    form_class = AreaForm
    success_url = reverse_lazy("municipalizacion:area_list")
    login_url = 'app:login'

class AreaDel(LoginRequiredMixin, generic.DeleteView):
    model = Area
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:area_list")
