from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import AusenBeneficiado
from app.forms import AusenBeneficiadoForm

class AusenBeneficiadoView(LoginRequiredMixin, generic.ListView):
    model = AusenBeneficiado
    template_name = 'educacion/ausbenefi_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class AusenBeneficiadoNew(LoginRequiredMixin, generic.CreateView):
    model = AusenBeneficiado
    template_name = "educacion/ausbenefi_form.html"
    context_object_name = "obj"
    form_class = AusenBeneficiadoForm
    success_url = reverse_lazy("educacion:ausbenefi_list")
    login_url = 'app:login'

class AusenBeneficiadoEdit(LoginRequiredMixin, generic.UpdateView):
    model = AusenBeneficiado
    template_name = "educacion/ausbenefi_form.html"
    context_object_name = "obj"
    form_class = AusenBeneficiadoForm
    success_url = reverse_lazy("educacion:ausbenefi_list")
    login_url = 'app:login'

class AusenBeneficiadoDel(LoginRequiredMixin, generic.DeleteView):
    model = AusenBeneficiado
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:ausbenefi_list")