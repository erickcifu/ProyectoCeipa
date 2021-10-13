from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.forms import inlineformset_factory

from app.models import Ciclo_grado, Ciclo
from app.forms import CGForm, CicloForm

def ciclo_gradoView(request, pk):
    queryset = Ciclo_grado.objects.all().filter(ciclo__id=pk)
    print("CONSULTA CICLO",queryset)
    context = {

        'grados_ciclo': queryset,
    }
    return render(request, 'educacion/cg_list.html', context)

class CGView(LoginRequiredMixin, generic.ListView):
    model = Ciclo_grado
    template_name = 'educacion/cg_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_queryset(self):
        qs = Ciclo_grado.objects.all()
        ciclo_id = self.request.GET.get("lang")
        if ciclo_id:
            qs = qs.filter(ciclo__id=ciclo_id)
        return qs

class CGNew(LoginRequiredMixin, generic.CreateView):
    model = Ciclo_grado
    template_name = 'educacion/cg_form.html'
    context_object_name = "obj"
    form_class = CGForm
    success_url = reverse_lazy("educacion:cg_list")
    login_url = 'app:login'

    def get_queryset(self):
        qs = Ciclo_grado.objects.all()
        ciclo_id = self.request.GET.get("lang")
        if ciclo_id:
            qs = qs.filter(ciclo__id=ciclo_id)
        return qs

class CGEdit(LoginRequiredMixin, generic.UpdateView):
    pass
    model = Ciclo_grado
    template_name = "educacion/cg_form.html"
    context_object_name = "obj"
    form_class = CGForm
    success_url = reverse_lazy("educacion:cg_list")
    login_url = 'app:login'

class CGDel(LoginRequiredMixin, generic.DeleteView):
    pass
    model = Ciclo_grado
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:cg_list")
