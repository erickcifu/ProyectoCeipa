from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Ausencia
from app.forms import AusenciaForm

class AusView(LoginRequiredMixin, generic.ListView):
    model = Ausencia
    template_name = 'municipalizacion/ausencia_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class AusNew(LoginRequiredMixin, generic.CreateView):
    model = Ausencia
    template_name = 'municipalizacion/ausencia_form.html'
    context_object_name = "obj"
    form_class = AusenciaForm
    success_url = reverse_lazy("municipalizacion:aus_list")
    login_url = 'app:login'

class AusEdit(LoginRequiredMixin, generic.UpdateView):
    model = Ausencia
    template_name = "municipalizacion/ausencia_form.html"
    context_object_name = "obj"
    form_class = AusenciaForm
    success_url = reverse_lazy("municipalizacion:aus_list")
    login_url = 'app:login'

class AusDel(LoginRequiredMixin, generic.DeleteView):
    model = Ausencia
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:aus_list")
