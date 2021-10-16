from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import BeneficiadoArea
from app.forms import BenefArForm

class BenefArView(LoginRequiredMixin, generic.ListView):
    model = BeneficiadoArea
    template_name = 'municipalizacion/benefar_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class BenefArNew(LoginRequiredMixin, generic.CreateView):
    model = BeneficiadoArea
    template_name = 'municipalizacion/benefar_form.html'
    context_object_name = "obj"
    form_class = BenefArForm
    success_url = reverse_lazy("municipalizacion:benefar_list")
    login_url = 'app:login'

class BenefArEdit(LoginRequiredMixin, generic.UpdateView):
    model = BeneficiadoArea
    template_name = "municipalizacion/benefar_form.html"
    context_object_name = "obj"
    form_class = BenefArForm
    success_url = reverse_lazy("municipalizacion:benefar_list")
    login_url = 'app:login'

class BenefArDel(LoginRequiredMixin, generic.DeleteView):
    model = BeneficiadoArea
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:benefar_list")
