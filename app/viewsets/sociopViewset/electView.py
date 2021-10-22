from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Electrodomesticos
from app.forms import ElectroForm

class ElectView(LoginRequiredMixin, generic.ListView):
    model = Electrodomesticos
    template_name = 'socioproductivo/elect_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ElectNew(LoginRequiredMixin, generic.CreateView):
    model = Electrodomesticos
    template_name = "socioproductivo/elect_form.html"
    context_object_name = "obj"
    form_class = ElectroForm
    success_url = reverse_lazy("socioproductivo:elect_list")
    login_url = 'app:login'

class ElectEdit(LoginRequiredMixin, generic.UpdateView):
    model = Electrodomesticos
    template_name = "socioproductivo/elect_form.html"
    context_object_name = "obj"
    form_class = ElectroForm
    success_url = reverse_lazy("socioproductivo:elect_list")
    login_url = 'app:login'

class ElectDel(LoginRequiredMixin, generic.DeleteView):
    model = Electrodomesticos
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:elect_list")
