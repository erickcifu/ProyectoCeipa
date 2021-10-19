from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Parentesco
from app.forms import ParentescoForm

class ParentescoView(LoginRequiredMixin, generic.ListView):
    model = Parentesco
    template_name = 'educacion/parentesco_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ParentescoNew(LoginRequiredMixin, generic.CreateView):
    model = Parentesco
    template_name = "educacion/parentesco_form.html"
    context_object_name = "obj"
    form_class = ParentescoForm
    success_url = reverse_lazy("educacion:parentesco_list")
    login_url = 'app:login'

class ParentescoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Parentesco
    template_name = "educacion/parentesco_form.html"
    context_object_name = "obj"
    form_class = ParentescoForm
    success_url = reverse_lazy("educacion:parentesco_list")
    login_url = 'app:login'

class ParentescoDel(LoginRequiredMixin, generic.DeleteView):
    model = Parentesco
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:parentesco_list")
