from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import ocupacion
from app.forms import OcupaForm

class OcupacionMuniView(LoginRequiredMixin, generic.ListView):
    model = ocupacion
    template_name = 'municipalizacion/ocupmuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class OcupacionMuniNew(LoginRequiredMixin, generic.CreateView):
    model = ocupacion
    template_name = "municipalizacion/ocupmuni_form.html"
    context_object_name = "obj"
    form_class = OcupaForm
    success_url = reverse_lazy("municipalizacion:ocupmuni_list")
    login_url = 'app:login'

class OcupacionMuniEdit(LoginRequiredMixin, generic.UpdateView):
    model = ocupacion
    template_name = "municipalizacion/ocupmuni_form.html"
    context_object_name = "obj"
    form_class = OcupaForm
    success_url = reverse_lazy("municipalizacion:ocupmuni_list")
    login_url = 'app:login'

class OcupacionMuniDel(LoginRequiredMixin, generic.DeleteView):
    model = ocupacion
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:ocupmuni_list")
