from django.db.models.query_utils import check_rel_lookup_compatibility
from django.shortcuts import render, redirect
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from app.viewsets.users.CoordinadorEducacion.mixin import IsCoordinadorEducacionMixin
from app.viewsets.users.mixins.CoordinadorGeneralYDirectorCentroMixin import RolesCoordinadorEducacionYDirectorCentroMixin
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

class CGView(IsCoordinadorEducacionMixin, generic.ListView):
    model = Ciclo_grado
    template_name = 'educacion/cg_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_queryset(self):
        qs = Ciclo_grado.objects.annotate(centro=F('ciclo_grado__centro_educativo__nombre_centro'))
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


class CGNew(IsCoordinadorEducacionMixin, generic.CreateView):
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
        '''
    def post(self, request, *args, **kwargs):
        self.id_ciclo = self.get_object()
        super().post(request, *args, **kwargs)
        '''
    def form_valid(self, form):
        self.id_ciclo = self.get_object()
        if form.is_valid():
            if self.id_ciclo:
                grado_ciclo = Ciclo_grado(**form.cleaned_data, ciclo=self.id_ciclo)
                grado_ciclo.save()
                print('se guardo',grado_ciclo)
                return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class CG_Del_Alumno(RolesCoordinadorEducacionYDirectorCentroMixin, generic.ListView):
    model = Ciclo_grado
    template_name = 'educacion/grados_del_alumno.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if self.request.user.user_profile.rol.id == 1 or self.request.user.user_profile.rol.id == 2:
                return [self.template_name]
            elif self.request.user.user_profile.rol.id == 5:
                return ["directorCentro/grados_del_alumno.html"]

    def get_object(self):
        id_alumno = self.kwargs.get('pk')
        if id_alumno:
            return Alumno.objects.filter(id=id_alumno).first()

    #devuelve todos los grados del alumno
    def get_queryset(self):
        id_alumno = self.kwargs.get("pk")
        if id_alumno:
            return Ciclo_grado.objects.filter(ciclo_grado__alumno_id = int(id_alumno))

        return None

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['alumno'] =  self.get_object()
        return context

class CGEdit(IsCoordinadorEducacionMixin, generic.UpdateView):
    pass
    model = Ciclo_grado
    template_name = "educacion/cg_form_update.html"
    context_object_name = "obj"
    form_class = CGForm
    success_url = reverse_lazy("educacion:cg_list")
    login_url = 'app:login'

class CGDel(IsCoordinadorEducacionMixin, generic.DeleteView):
    pass
    model = Ciclo_grado
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:cg_list")


class CiclosForCreateGradeandCourseView(IsCoordinadorEducacionMixin, generic.ListView):
    model = Ciclo
    template_name = 'prueba/ciclos.html'
    context_object_name = 'obj'
    login_url = 'app:login'
