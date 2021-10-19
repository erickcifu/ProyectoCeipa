from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import vivienda
from app.forms import VivForm

class VivView(LoginRequiredMixin, generic.ListView):
    model = vivienda
    template_name = 'educacion/viv_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class VivNew(LoginRequiredMixin, generic.CreateView):
    model = vivienda
    template_name = "educacion/viv_form.html"
    context_object_name = "obj"
    form_class = VivForm
    success_url = reverse_lazy("educacion:viv_list")
    login_url = 'app:login'

class VivEdit(LoginRequiredMixin, generic.UpdateView):
    model = vivienda
    template_name = "educacion/viv_form.html"
    context_object_name = "obj"
    form_class = VivForm
    success_url = reverse_lazy("educacion:viv_list")
    login_url = 'app:login'

class VivDel(LoginRequiredMixin, generic.DeleteView):
    model = vivienda
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:viv_list")
