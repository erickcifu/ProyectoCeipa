from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from app.models import Maestro, Persona, IdiomaPersona
from app.forms import MaestroForm, PersonaForm,IdPerForm
from django.db import IntegrityError, transaction
from django.forms import formset_factory
from app.models.educacion_model.idioma import idioma

class MaesView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = Maestro
    template_name = 'municipalizacion/maerstro_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class MaesNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = Maestro
    template_name = 'municipalizacion/maerstro_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = MaestroForm
    third_form_class = formset_factory(IdPerForm, extra=1)
    success_url = reverse_lazy("municipalizacion:maes_list")
    login_url = 'app:login'

    def get_template_names(self):
        user = self.request.user.user_profile.rol.id
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if user == 7 or user == 8:
                return [self.template_name]
            elif user == 9:
                return ["equipoMunicipal/maerstro_form.html"]
            else:
                return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super(MaesNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(prefix = 'idiomas_maestro')
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(Maestro, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                self.object = self.get_object
                form = self.form_class(request.POST, request.FILES)
                form2 = self.second_form_class(request.POST)
                form3 = self.third_form_class(request.POST, prefix = 'idiomas_maestro')
                if form.is_valid() and form2.is_valid() and form3.is_valid():
                    persona = form.save()
                    maestro= form2.save(commit=False)
                    maestro.persona_maestro = persona
                    maestro.save()
                    for idi_maestro in form3:
                        idioma = idi_maestro.save(commit=False)
                        idioma.persona = persona
                        idioma.save()
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))
        except IntegrityError:
            return HttpResponseRedirect("ERROR: No se puede registrar al participante")


class MaesEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    model = Maestro
    template_name = "municipalizacion/maerstro_edit.html"
    form_class = PersonaForm
    second_form_class = MaestroForm
    third_form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:maes_list")
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_maestro'] = self.second_form_class
        context['obj'] = ''
        return context

    def post(self, request, *args, **kwargs):
        maestro = self.get_object()
        persona_maestro = maestro.persona_maestro
        idioma = IdiomaPersona.objects.filter(persona=persona_maestro)

        form = self.form_class(request.POST, instance = persona_maestro)
        form2 = self.second_form_class(request.POST, instance = maestro)

        with transaction.atomic():
            for idi_maestro in idioma:
                form3 = self.third_form_class(request.POST, instance = idi_maestro, prefix='idiomas_maestro')
                if form3.is_valid():
                    form3.save()
            if form.is_valid() and form2.is_valid():
                form.save()
                form2.save()
                form3.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

    def get(self, request, *args, **kwargs):
        maestro = self.get_object()
        persona_maestro = maestro.persona_maestro

        try:
            formid_maestro = formset_factory(IdPerForm, extra=0)
            listado_idmaestro = []
            idiom_maestro = IdiomaPersona.objects.filter(persona=persona_maestro)
            for id_ma in idiom_maestro:
                listado_idmaestro.append({
                    'idioma':i.idioma.id,
                    'estado_ip':i.estado_ip
                })
            formset_idmaestro = formid_maestro(initial=listado_idmaestro, prefix='idiomas_maestro')
        except:
            print("Ocurrió un error")
            return HttpResponseRedirect(self.success_url)
        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = maestro)
        if 'form3' not in context:
            context['form3'] = formset_idmaestro
        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)

class MaesDetail(LoginRequiredMixin, generic.DetailView):
    template_name = "municipalizacion/maestro_detail.html"
    model = Maestro

    def get_idioma(self, persona_maestro):
        return IdiomaPersona.objects.filter(persona=persona_maestro)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        maestro = self.get_object()
        persona_maestro = maestro.persona_maestro
        context['item'] = maestro
        context['persona_maestro'] = persona_maestro
        context['idioma_maestro'] = self.get_idioma(persona_maestro)
        return context


class MaesDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = Maestro
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:maes_list")
