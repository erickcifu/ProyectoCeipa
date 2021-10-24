from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Taller
from app.forms import TallerForm

class TallerView(LoginRequiredMixin, generic.ListView):
    model = Taller
    template_name = 'socioproductivo/talleres_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class TallerNew(LoginRequiredMixin, generic.CreateView):
    model = Taller
    template_name = "socioproductivo/talleres_form.html"
    context_object_name = "obj"
    form_class = TallerForm
    success_url = reverse_lazy("socioproductivo:talleres_list")
    login_url = 'app:login'

class TallerEdit(LoginRequiredMixin, generic.UpdateView):
    model = Taller
    template_name = "socioproductivo/talleres_form.html"
    context_object_name = "obj"
    form_class = TallerForm
    success_url = reverse_lazy("socioproductivo:talleres_list")
    login_url = 'app:login'

class TallerDel(LoginRequiredMixin, generic.DeleteView):
    model = Taller
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:talleres_list")
