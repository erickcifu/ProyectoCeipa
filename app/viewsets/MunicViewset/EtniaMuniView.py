from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import etnia
from app.forms import EtniaForm

class EtnMuniView(LoginRequiredMixin, generic.ListView):
    model = etnia
    template_name = 'municipalizacion/etniamuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class EtniaMuniNew(LoginRequiredMixin, generic.CreateView):
    model = etnia
    template_name = "municipalizacion/etniamuni_form.html"
    context_object_name = "obj"
    form_class = EtniaForm
    success_url = reverse_lazy("municipalizacion:etniamuni_list")
    login_url = 'app:login'

class EtniaMuniEdit(LoginRequiredMixin, generic.UpdateView):
    model = etnia
    template_name = "municipalizacion/etniamuni_form.html"
    context_object_name = "obj"
    form_class = EtniaForm
    success_url = reverse_lazy("municipalizacion:etniamuni_list")
    login_url = 'app:login'

class EtniaMuniDel(LoginRequiredMixin, generic.DeleteView):
    model = etnia
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:etniamuni_list")
