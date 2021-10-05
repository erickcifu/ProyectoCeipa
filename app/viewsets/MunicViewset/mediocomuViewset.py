from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import MedioComuni
from app.forms import MedioComuniForm

class MedioComuniView(LoginRequiredMixin, generic.ListView):
    model = MedioComuni
    template_name = 'municipalizacion/mediocomu_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class MedioComuniNew(LoginRequiredMixin, generic.CreateView):
    model = MedioComuni
    template_name = "municipalizacion/mediocomu_form.html"
    context_object_name = "obj"
    form_class = MedioComuniForm
    success_url = reverse_lazy("municipalizacion:mediocomu_list")
    login_url = 'app:login'

class MedioComuniEdit(LoginRequiredMixin, generic.UpdateView):
    model = MedioComuni
    template_name = "municipalizacion/mediocomu_form.html"
    context_object_name = "obj"
    form_class = MedioComuniForm
    success_url = reverse_lazy("municipalizacion:mediocomu_list")
    login_url = 'app:login'

class MedioComuniDel(LoginRequiredMixin, generic.DeleteView):
    model = MedioComuni
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:mediocomu_list")