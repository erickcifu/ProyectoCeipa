from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import ElectVivienda
from app.forms import ElectvivForm

class ElectvivView(LoginRequiredMixin, generic.ListView):
    model = ElectVivienda
    template_name = 'socioproductivo/electviv_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ElectvivNew(LoginRequiredMixin, generic.CreateView):
    model = ElectVivienda
    template_name = "socioproductivo/electviv_form.html"
    context_object_name = "obj"
    form_class = ElectvivForm
    success_url = reverse_lazy("socioproductivo:electviv_list")
    login_url = 'app:login'

class ElectvivEdit(LoginRequiredMixin, generic.UpdateView):
    model = ElectVivienda
    template_name = "socioproductivo/electviv_form.html"
    context_object_name = "obj"
    form_class = ElectvivForm
    success_url = reverse_lazy("socioproductivo:electviv_list")
    login_url = 'app:login'

class ElectvivDel(LoginRequiredMixin, generic.DeleteView):
    model = ElectVivienda
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:electviv_list")
