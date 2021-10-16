from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Centropersona
from app.forms import CentPerForm

class CentPerView(LoginRequiredMixin, generic.ListView):
    model = Centropersona
    template_name = 'educacion/centper_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class CentPerNew(LoginRequiredMixin, generic.CreateView):
    model = Centropersona
    template_name = "educacion/centper_form.html"
    context_object_name = "obj"
    form_class = CentPerForm
    success_url = reverse_lazy("educacion:centper_list")
    login_url = 'app:login'

class CentPerEdit(LoginRequiredMixin, generic.UpdateView):
    model = Centropersona
    template_name = "educacion/centper_form.html"
    context_object_name = "obj"
    form_class = CentPerForm
    success_url = reverse_lazy("educacion:centper_list")
    login_url = 'app:login'

class CentPerDel(LoginRequiredMixin, generic.DeleteView):
    model = Centropersona
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:centper_list")
