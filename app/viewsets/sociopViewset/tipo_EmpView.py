from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import TipoEmp
from app.forms import TipoEmpForm

class TipoEmpView(LoginRequiredMixin, generic.ListView):
    model = TipoEmp
    template_name = 'socioproductivo/TipoEmp_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class TipoEmpNew(LoginRequiredMixin, generic.CreateView):
    model = TipoEmp
    template_name = "socioproductivo/TipoEmp_form.html"
    context_object_name = "obj"
    form_class = TipoEmpForm
    success_url = reverse_lazy("socioproductivo:TipoEmp_list")
    login_url = 'app:login'

class TipoEmpEdit(LoginRequiredMixin, generic.UpdateView):
    model = TipoEmp
    template_name = "socioproductivo/TipoEmp_form.html"
    context_object_name = "obj"
    form_class = TipoEmpForm
    success_url = reverse_lazy("socioproductivo:TipoEmp_list")
    login_url = 'app:login'

class TipoEmpDel(LoginRequiredMixin, generic.DeleteView):
    model = TipoEmp
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:TipoEmp_list")
