from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import AspectosSalud
from app.forms import AspectosSaludForm

class AspectosSaludView(LoginRequiredMixin, generic.ListView):
    model = AspectosSalud
    template_name = 'socioproductivo/aspectos_salud_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class AspectosSaludNew(LoginRequiredMixin, generic.CreateView):
    model = AspectosSalud
    template_name = "socioproductivo/aspectos_salud_form.html"
    context_object_name = "obj"
    form_class = AspectosSaludForm
    success_url = reverse_lazy("socioproductivo:aspectos_salud_list")
    login_url = 'app:login'

class AspectosSaludEdit(LoginRequiredMixin, generic.UpdateView):
    model = AspectosSalud
    template_name = "socioproductivo/aspectos_salud_form.html"
    context_object_name = "obj"
    form_class = AspectosSaludForm
    success_url = reverse_lazy("socioproductivo:aspectos_salud_list")
    login_url = 'app:login'

class AspectosSaludDel(LoginRequiredMixin, generic.DeleteView):
    model = AspectosSalud
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:aspectos_salud_list")
