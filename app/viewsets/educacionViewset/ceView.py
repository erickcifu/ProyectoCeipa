from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, OuterRef, Subquery, IntegerField

from django.views import generic
from django.urls import reverse_lazy
from django.forms import inlineformset_factory

from app.models import Ciclo_etapa, Ciclo, Alumno
from django.db.models import F
from app.forms import CEForm, CEFormCreate


class CEView(LoginRequiredMixin, generic.ListView):
    model = Ciclo_etapa
    template_name = 'educacion/ce_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_queryset(self):
        qs = Ciclo_etapa.objects.annotate(centro=F('ce_insc__centro_educ_etapa__nombre_centro'))
        ciclo_id = self.request.GET.get("ciclo_e")
        if ciclo_id:
            qs = qs.filter(ciclo_c__id=ciclo_id)
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

class CENew(LoginRequiredMixin, generic.CreateView):
    model = Ciclo_etapa
    template_name = 'educacion/ce_form.html'
    context_object_name = "obj"
    form_class = CEFormCreate
    success_url = reverse_lazy("educacion:ce_list")
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
    '''
    def post(self, request, *args, **kwargs):
        self.id_ciclo = self.get_object()
        super().post(request, *args, **kwargs)
    '''

    def form_valid(self, form):
        if form.is_valid():
            self.id_ciclo = self.get_object()
            if self.id_ciclo:
                etapa_ciclo = Ciclo_etapa(**form.cleaned_data, ciclo_c=self.id_ciclo)
                etapa_ciclo.save()
                print('se guardo',etapa_ciclo)
                return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class Etapas_Del_Alumno(LoginRequiredMixin, generic.ListView):
    model = Ciclo_etapa
    template_name = 'educacion/etapas_del_alumno.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_object(self):
        id_alumno = self.kwargs.get('pk')
        if id_alumno:
            return Alumno.objects.filter(id=id_alumno).first()

    #devuelve todas las etapas del alumno
    def get_queryset(self):
        id_alumno = self.kwargs.get("pk")
        if id_alumno:
            return Ciclo_etapa.objects.filter(ce_insc__alumno_etapa_id = int(id_alumno))

        return None

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['alumno'] =  self.get_object()
        return context
