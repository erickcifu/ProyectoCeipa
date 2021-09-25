from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from .models.educacion_model.parentesco import Parentesco
from .models.educacion_model.departamento import departamento
from .models.educacion_model.municipioModel import municipio
from .forms import DepartamentoForm, ParentescoForm, MunicipioForm

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app/home.html'
    login_url = 'app:login'


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

class DepartamentoView(LoginRequiredMixin, generic.ListView):
    model = departamento
    template_name = 'educacion/departamento_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class DepartamentoNew(LoginRequiredMixin, generic.CreateView):
    model = departamento
    template_name = "educacion/departamento_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_url = reverse_lazy("educacion:departamento_list")
    login_url = 'app:login'

class DepartamentoEdit(LoginRequiredMixin, generic.UpdateView):
    model = departamento
    template_name = "educacion/departamento_form.html"
    context_object_name = "obj"
    form_class = DepartamentoForm
    success_url = reverse_lazy("educacion:departamento_list")
    login_url = 'app:login'

class DepartamentoDel(LoginRequiredMixin, generic.DeleteView):
    model = departamento
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:departamento_list")

class MunicipioView(LoginRequiredMixin, generic.ListView):
    model = municipio
    template_name = 'educacion/municipio_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class MunicipioNew(LoginRequiredMixin, generic.CreateView):
    model = municipio
    template_name = "educacion/municipio_form.html"
    context_object_name = "obj"
    form_class = MunicipioForm
    success_url = reverse_lazy("educacion:municipio_list")
    login_url = 'app:login'

class MunicipioEdit(LoginRequiredMixin, generic.UpdateView):
    model = municipio
    template_name = "educacion/municipio_form.html"
    context_object_name = "obj"
    form_class = MunicipioForm
    success_url = reverse_lazy("educacion:municipio_list")
    login_url = 'app:login'

class MunicipioDel(LoginRequiredMixin, generic.DeleteView):
    model = municipio
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:municipio_list")