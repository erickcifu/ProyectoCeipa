from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import InfoEducacion
from app.forms import InfoEducacionForm

class InfoEducacionView(LoginRequiredMixin, generic.ListView):
    model = InfoEducacion
    template_name = 'socioproductivo/infoeducacion_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class InfoEducacionNew(LoginRequiredMixin, generic.CreateView):
    model = InfoEducacion
    template_name = "socioproductivo/infoeducacion_form.html"
    context_object_name = "obj"
    form_class = InfoEducacionForm
    success_url = reverse_lazy("socioproductivo:infoeducacion_list")
    login_url = 'app:login'

class InfoEducacionEdit(LoginRequiredMixin, generic.UpdateView):
    model = InfoEducacion
    template_name = "socioproductivo/infoeducacion_form.html"
    context_object_name = "obj"
    form_class = InfoEducacionForm
    success_url = reverse_lazy("socioproductivo:infoeducacion_list")
    login_url = 'app:login'

class InfoEducacionDel(LoginRequiredMixin, generic.DeleteView):
    model = InfoEducacion
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:infoeducacion_list")