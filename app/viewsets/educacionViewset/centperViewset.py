from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from app.forms.educacionForms.centroPerForm import CentPerPorCentroEducativoForm

from app.models import Centropersona, centro_educativo
from app.forms import CentPerForm
from app.models.educacion_model.personalEducativo import personalEducativo

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