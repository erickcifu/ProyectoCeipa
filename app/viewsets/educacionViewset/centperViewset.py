from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from app.viewsets.users.CoordinadorEducacion.mixin import IsCoordinadorEducacionMixin
from app.viewsets.users.maestro.mixin import IsMaestroMixin
from django.views import generic
from django.urls import reverse_lazy
from app.forms.educacionForms.centroPerForm import CentPerPorCentroEducativoForm, AsignarDirectorCentroEducativoForm

from app.models import Centropersona, centro_educativo, personalEducativo
from app.forms import CentPerForm

class CentPerView(LoginRequiredMixin, generic.ListView):
    model = Centropersona
    template_name = 'educacion/centper_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class CentPerNew(LoginRequiredMixin, generic.CreateView):
    model = Centropersona
    template_name = "educacion/centper_form.html"
    context_object_name = "obj"
    form_class = CentPerForm
    success_url = reverse_lazy("educacion:centper_list")
    login_url = 'app:login'

class CentPerEdit(LoginRequiredMixin, generic.UpdateView):
    model = Centropersona
    template_name = "educacion/centper_form.html"
    context_object_name = "obj"
    form_class = CentPerForm
    success_url = reverse_lazy("educacion:centper_list")
    login_url = 'app:login'

class CentPerDel(LoginRequiredMixin, generic.DeleteView):
    model = Centropersona
    template_name = "educacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("educacion:centper_list")

class ListarDirectoresPorCentroEducativo(IsCoordinadorEducacionMixin, generic.ListView):
    model = Centropersona
    template_name = "educacion/listarDirectoresCentro.html"
    context_object_name = "obj"

    def get_queryset(self):
        qs = Centropersona.objects.filter(personal__perfile__rol_id=5)
        centro = self.request.GET.get("id_centro_educativo")
        if centro:
            qs = qs.filter(centro_Educativo_id=int(centro))
        return qs

    def get_object(self):
        centro = self.request.GET.get("id_centro_educativo")
        if centro:
            return centro_educativo.objects.filter(id=int(centro)).first()
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_centro_educativo'] = self.get_object()
        context['centros_educativos'] = centro_educativo.objects.all()

        return context

class AsignarDirectorACentroEducativo(IsCoordinadorEducacionMixin, generic.CreateView):
    model = Centropersona
    form_class = AsignarDirectorCentroEducativoForm
    template_name = 'educacion/asignar_director_centro_form.html'
    success_url = reverse_lazy("educacion:centper_list")
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_object(self):
        centro = self.kwargs.get("pk")
        if centro:
            return centro_educativo.objects.filter(id=int(centro)).first()
        return None

    def post(self, request, *args, **kwargs):
        form = CentPerPorCentroEducativoForm(request.POST)
        if form.is_valid():
            centro_edu = self.get_object()
            if centro_edu:
                Centropersona.objects.create(**form.cleaned_data, centro_Educativo=centro_edu)
                return HttpResponseRedirect(self.success_url)
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_centro_educativo'] = self.get_object()
        context['centros_educativos'] = centro_educativo.objects.all()
        context['maestros'] = personalEducativo.objects.filter(perfile__rol_id=5).exclude(p_educativo__centro_Educativo__id__in = centro_educativo.objects.values_list('id'))
        return context


class AsignarPersonalEducativoCentroPersona(LoginRequiredMixin, generic.CreateView):
    model = Centropersona
    template_name = "educacion/centerdu_form_por_centro_educativo.html"
    context_object_name = "obj"
    form_class = CentPerPorCentroEducativoForm
    success_url = reverse_lazy("educacion:listado_personal_por_centro_educativo")
    login_url = 'app:login'

    def get_object(self):
        id_centro_educativo = self.kwargs.get('pk')
        if id_centro_educativo:
            return centro_educativo.objects.filter(id=int(id_centro_educativo)).first()
        return None

    def post(self, request, *args, **kwargs):
        form = CentPerPorCentroEducativoForm(request.POST)
        if form.is_valid():
            centro_edu = self.get_object()
            if centro_edu:
                Centropersona.objects.create(**form.cleaned_data, centro_Educativo=centro_edu)
                return HttpResponseRedirect(self.success_url)
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_centro_educativo'] = self.get_object()
        context['centros_educativos'] = centro_educativo.objects.all()
        context['maestros'] = personalEducativo.objects.exclude(p_educativo__centro_Educativo__id = self.get_object().id)

        return context

#rol maestro
class ListarCentroEducativoPorMaestro(IsMaestroMixin, generic.ListView):
    model = centro_educativo
    template_name = 'maestro/centedu_list.html'
    context_object_name = 'obj'

    def get_queryset(self):
        user = self.request.user
        return centro_educativo.objects.filter(c_educativo__personal__perfile = user.user_profile)
