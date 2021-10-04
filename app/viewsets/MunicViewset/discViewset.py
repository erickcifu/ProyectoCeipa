from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Discapacidad
from app.forms import DiscForm

class DiscView(LoginRequiredMixin, generic.ListView):
    model = Discapacidad
    template_name = 'municipalizacion/disc_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class DiscNew(LoginRequiredMixin, generic.CreateView):
    model = Discapacidad
    template_name = 'municipalizacion/disc_form.html'
    context_object_name = "obj"
    form_class = DiscForm
    success_url = reverse_lazy("municipalizacion:disc_list")
    login_url = 'app:login'

class DiscEdit(LoginRequiredMixin, generic.UpdateView):
    model = Discapacidad
    template_name = "municipalizacion/disc_form.html"
    context_object_name = "obj"
    form_class = DiscForm
    success_url = reverse_lazy("municipalizacion:disc_list")
    login_url = 'app:login'

class DiscDel(LoginRequiredMixin, generic.DeleteView):
    model = Discapacidad
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:disc_list")
