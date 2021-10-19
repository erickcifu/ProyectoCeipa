from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.forms import inlineformset_factory

from app.models import Ciclo_grado, Ciclo, Alumno
from django.db.models import F
from app.forms import CGForm, CGFormCreate

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
        ciclo_id = self.request.GET.get("ciclo")
        if ciclo_id:
            qs = qs.filter(ciclo__id=ciclo_id)
        print(qs)
        return qs

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['ciclos'] = Ciclo.objects.filter(estado_ciclo=True)
        id_ciclo = None
        if self.request.GET.get("ciclo"):
            id_ciclo = Ciclo.objects.filter(id=int(self.request.GET.get("ciclo"))).first()
        context['id_ciclo'] =  id_ciclo
        return context
    

class CGNew(LoginRequiredMixin, generic.CreateView):
    model = Ciclo_grado
    template_name = 'educacion/cg_form.html'
    context_object_name = "obj"
    form_class = CGFormCreate
    success_url = reverse_lazy("educacion:cg_list")
    login_url = 'app:login'
    id_ciclo = ''

    def get_queryset(self):
        return Ciclo.objects.all()
        
    
    def get_object(self):
        ciclo_id = self.kwargs.get('pk')
        qs = None
        if ciclo_id:
            qs = self.get_queryset().filter(id=ciclo_id).first()
        
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_ciclo'] = self.get_object().id if self.get_object() else ''
        context['ciclos'] = Ciclo.objects.all()
        return context
    
    def post(self, request, *args, **kwargs):
        self.id_ciclo = self.get_object()
        super().post(request, *args, **kwargs)    

    def form_valid(self, form):
        if form.is_valid():
            if self.id_ciclo:
                grado_ciclo = Ciclo_grado(**form.cleaned_data, ciclo=self.id_ciclo)
                grado_ciclo.save()
                print('se guardo',grado_ciclo)
                return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))        


class CGEdit(LoginRequiredMixin, generic.UpdateView):
    pass
    model = Ciclo_grado
    template_name = "educacion/cg_form_update.html"
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


class CiclosForCreateGradeandCourseView(LoginRequiredMixin, generic.ListView):
    model = Ciclo
    template_name = 'prueba/ciclos.html'
    context_object_name = 'obj'
    login_url = 'app:login'

