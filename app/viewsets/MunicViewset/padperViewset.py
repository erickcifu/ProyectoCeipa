from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import PadPer
from app.forms import PadPerForm

class PadPerView(LoginRequiredMixin, generic.ListView):
    model = PadPer
    template_name = 'municipalizacion/padper_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PadPerNew(LoginRequiredMixin, generic.CreateView):
    model = PadPer
    template_name = 'municipalizacion/padper_form.html'
    context_object_name = "obj"
    form_class = PadPerForm
    success_url = reverse_lazy("municipalizacion:padper_list")
    login_url = 'app:login'

class PadPerEdit(LoginRequiredMixin, generic.UpdateView):
    model = PadPer
    template_name = "municipalizacion/padper_form.html"
    context_object_name = "obj"
    form_class = PadPerForm
    success_url = reverse_lazy("municipalizacion:padper_list")
    login_url = 'app:login'

class PadPerDel(LoginRequiredMixin, generic.DeleteView):
    model = PadPer
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:padper_list")
