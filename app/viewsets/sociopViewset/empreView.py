from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorSocioProductivo.mixin import IsCoordinadorSocioProductivoMixin
from app.viewsets.users.mixins.CooSocioproductivoYEquipoSocioproductivo import RolesCoordinadorSocioproductivoYEquipoSocioproductivo
from app.models import Emprendimiento, PersonaBasica
from app.forms import EmprenForm

class EmprenView(IsCoordinadorSocioProductivoMixin, generic.ListView):
    model = Emprendimiento
    template_name = 'socioproductivo/Emprendimiento_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class EmprenNew(RolesCoordinadorSocioproductivoYEquipoSocioproductivo, generic.CreateView):
    model = Emprendimiento
    template_name = "socioproductivo/Emprendimiento_form.html"
    context_object_name = "obj"
    form_class = EmprenForm
    success_url = reverse_lazy("socioproductivo:emprend_list")
    login_url = 'app:login'
    id_persona = ''

    def get_template_names(self):
        user = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if user == 10 or user == 11:
                return [self.template_name]
            elif user == 12:
                return ["equipoSocioproductivo/Emprendimiento_form.html"]
            else:
                return [self.template_name]

    def form_valid(self, form):
        form.save()
        if self.request.user.user_profile.rol.id == 12:
            return redirect('socioproductivo:home_equipo_socioproductivo')
        return redirect("socioproductivo:emprend_list")

    def get_queryset(self):
        return PersonaBasica.objects.all()

    def get_object(self):
        persona_id = self.kwargs.get('pk')
        qs = None
        if persona_id:
            qs = self.get_queryset().filter(id=persona_id).first()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_persona'] = self.get_object().id if self.get_object() else ''
        context['personas'] = PersonaBasica.objects.all()
        return context

    def form_valid(self, form):
        if form.is_valid():
            self.id_persona = self.get_object()
            if self.id_persona:
                emprendimiento_persona = Emprendimiento(**form.cleaned_data, persona=self.id_persona)
                emprendimiento_persona.save()
                print('se guardó', emprendimiento_persona)
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form))

class EmprenEdit(IsCoordinadorSocioProductivoMixin, generic.UpdateView):
    model = Emprendimiento
    template_name = "socioproductivo/Empren_form.html"
    context_object_name = "obj"
    form_class = EmprenForm
    success_url = reverse_lazy("socioproductivo:emprend_list")
    login_url = 'app:login'

class EmprenDel(IsCoordinadorSocioProductivoMixin, generic.DeleteView):
    model = Emprendimiento
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:emprend_list")
