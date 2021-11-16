from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin
from django.views.decorators.csrf import csrf_exempt
from app.models import CorporacionMunicipal, Persona, IdiomaPersona
from app.forms import CorpMuniForm, PersonaForm, IdPerForm
from app.models.educacion_model.idioma import idioma
from django.forms import formset_factory
from django.db import IntegrityError, transaction

class CorpMuniView(RolesCooMunicipalEquipoMunicipalMixin, generic.ListView):
    model = CorporacionMunicipal
    template_name = 'municipalizacion/corpmuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "TemplateResponseMixin requires either a definition of "
                "'template_name' or an implementation of 'get_template_names()'")
        else:
            if self.request.user.user_profile.rol.id == 7 or self.request.user.user_profile.rol.id == 8:
                return [self.template_name]
            elif self.request.user.user_profile.rol.id == 9:
                return ["equipoMunicipal/corpmuni_list.html"]

class CorpMuniNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = CorporacionMunicipal
    template_name = 'municipalizacion/corpmuni_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = CorpMuniForm
    third_form_class = formset_factory(IdPerForm, extra=1)
    success_url = reverse_lazy("municipalizacion:corpmuni_list")
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
                return ["equipoMunicipal/corpmuni_form.html"]
            else:
                return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super(CorpMuniNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        if 'form3' not in context:
            context['form3'] = self.third_form_class(prefix='idiomas_corp')
        context['errors_forms'] = {}
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(Maestro, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST, prefix='idiomas_corp')
        try:
            with transaction.atomic():
                if form.is_valid() and form2.is_valid() and form3.is_valid():
                    persona = form.save()
                    CorpMuniForm= form2.save(commit=False)
                    CorpMuniForm.persona = persona
                    CorpMuniForm.save()
                    if len(form3.cleaned_data) == 1:
                        if form3.cleaned_data[0]:
                            for corp_idiomas in form3:
                                idioma = corp_idiomas.save(commit=False)
                                idioma.persona = persona
                                idioma.save()
                    elif len(form3.cleaned_data) >=1:
                        for corp_idiomas in form3:
                            if corp_idiomas.cleaned_data:
                                idioma = corp_idiomas.save(commit=False)
                                idioma.persona = persona
                                idioma.save()
                    if self.request.user.user_profile.rol.id == 9:
                        return redirect('educacion:home_equipo_municipal')

                    return HttpResponseRedirect(self.get_success_url())
                else:
                    print(form2.errors)
                    errors = {
                        'form':{'erros':form.errors, 'name':'Persona'},
                        'form2':{'erros':form2.errors, 'name':'CorporacionMunicipal'},
                        'form3':{'erros':form3.errors, 'name':'IdiomaPersona'},
                    }
                    print(errors)
                    return self.render_to_response(self.get_context_data(form=form,
                        form2=form2,
                        form3=form3,
                    ))
        except IntegrityError:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))


class CorpMuniEdit(RolesCooMunicipalEquipoMunicipalMixin, generic.UpdateView):
    model = CorporacionMunicipal
    template_name = "municipalizacion/corpmuni_edit.html"
    form_class = PersonaForm
    second_form_class = CorpMuniForm
    third_form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:corpmuni_list")
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
                return ["equipoMunicipal/corpmuni_edit.html"]
            else:
                return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_corp'] = self.second_form_class
        context['obj'] = ''
        return context

    def post(self, request, *args, **kwargs):
        corpmuni = self.get_object()
        persona_corpmuni = corpmuni.persona
        idioma_corpmuni = IdiomaPersona.objects.filter(persona=persona_corpmuni)

        form = self.form_class(request.POST, request.FILES, instance = persona_corpmuni)
        form2 = self.second_form_class(request.POST, instance = corpmuni)

        with transaction.atomic():
            for idioma_corp in idioma_corpmuni:
                form3 = self.third_form_class(request.POST, instance=idioma_corp, prefix='idiomas_corp')
                if form3.is_valid():
                    form3.save()
            if form.is_valid() and form2.is_valid():
                form.save()
                form2.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

    def get(self, request, *args, **kwargs):
        corpmuni = self.get_object()
        persona_corpmuni = corpmuni.persona

        try:
            formid_corp = formset_factory(IdPerForm, extra=0)
            listadoid_corp = []
            idiom_corp = IdiomaPersona.objects.filter(persona=persona_corpmuni)
            for i_corp in idiom_corp:
                listadoid_corp.append({
                    'idioma': i_corp.idioma.id,
                    'estado_ip': i_corp.estado_ip,
                })
            formset_idcorp = formid_corp(initial=listadoid_corp, prefix='idiomas_corp')
        except:
            print("error")
            return HttpResponseRedirect(self.success_url)
        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona_corpmuni)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = corpmuni)
        if 'form3' not in context:
            context['form3'] = formset_idcorp
        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)
class CorpMuniDetail(RolesCooMunicipalEquipoMunicipalMixin, generic.DetailView):
    template_name = "municipalizacion/corpmuni_detail.html"
    model = CorporacionMunicipal

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
                return ["equipoMunicipal/corpmuni_detail.html"]
            else:
                return [self.template_name]

    def get_idioma_corp(self, persona_corpmuni):
        return IdiomaPersona.objects.filter(persona=persona_corpmuni)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        corpmuni = self.get_object()
        persona_corpmuni = corpmuni.persona
        context['item'] = corpmuni
        context['persona_corpmuni'] = persona_corpmuni
        context['idioma_corp'] = self.get_idioma_corp(persona_corpmuni)
        return context

class CorpMuniDel(LoginRequiredMixin, generic.DeleteView):
    model = CorporacionMunicipal
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:corpmuni_list")
