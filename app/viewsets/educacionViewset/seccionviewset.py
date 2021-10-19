from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import seccion
from app.forms import SeccionForm

class SeccionView(LoginRequiredMixin, generic.ListView):
    model = seccion
    template_name = 'educacion/seccion_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class SeccionNew(LoginRequiredMixin, generic.CreateView):
    model = seccion
    template_name = "educacion/seccion_form.html"
    context_object_name = "obj"
    form_class = SeccionForm
    success_url = reverse_lazy("educacion:seccion_list")
    login_url = 'app:login'

class SeccionEdit(LoginRequiredMixin, generic.UpdateView):
    model = seccion
    template_name = "educacion/seccion_form.html"
    context_object_name = "obj"
    form_class = SeccionForm
    success_url = reverse_lazy("educacion:seccion_list")
    login_url = 'app:login'

class SeccionDel(LoginRequiredMixin, generic.DeleteView):
    model = seccion
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:seccion_list")
