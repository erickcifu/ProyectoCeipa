from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import ocupacion
from app.forms import OcupaForm

class OcupView(LoginRequiredMixin, generic.ListView):
    model = ocupacion
    template_name = 'educacion/ocup_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class OcupNew(LoginRequiredMixin, generic.CreateView):
    model = ocupacion
    template_name = "educacion/ocup_form.html"
    context_object_name = "obj"
    form_class = OcupaForm
    success_url = reverse_lazy("educacion:ocup_list")
    login_url = 'app:login'

class OcupEdit(LoginRequiredMixin, generic.UpdateView):
    model = ocupacion
    template_name = "educacion/ocup_form.html"
    context_object_name = "obj"
    form_class = OcupaForm
    success_url = reverse_lazy("educacion:ocup_list")
    login_url = 'app:login'

class OcupDel(LoginRequiredMixin, generic.DeleteView):
    model = ocupacion
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:ocup_list")
