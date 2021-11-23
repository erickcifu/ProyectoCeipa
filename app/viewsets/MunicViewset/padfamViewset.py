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
from django.db import IntegrityError, transaction
from django.forms import formset_factory
from app.models import PadresFamilia, IdiomaPersona, Persona
from app.forms import PadFamForm, IdPerForm, PersonaForm

class PadFamView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = PadresFamilia
    template_name = 'municipalizacion/padfam_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PadFamNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = PadresFamilia
    template_name = 'municipalizacion/padfam_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = PadFamForm
    third_form_class = formset_factory(IdPerForm, extra=1)
    success_url = reverse_lazy("municipalizacion:padfam_list")
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
                return ["equipoMunicipal/padfam_form.html"]
            else:
                return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super(PadFamNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        if 'form3' not in context:
            context['form3'] = self.third_form_class(prefix = 'idiomas_padres')

        context['errors_forms'] = {}
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(PadresFamilia, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, request.FILES)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST, prefix = 'idiomas_padres')
        try:
            with transaction.atomic():
                if form.is_valid() and form2.is_valid() and form3.is_valid():
                    persona = form.save()
                    padfam = form2.save(commit=False)
                    padfam.persona = persona
                    padfam.save()
                    if len(form3.cleaned_data) == 1:
                        if form3.cleaned_data[0]:
                            for idi_padres in form3:
                                idioma = idi_padres.save(commit=False)
                                idioma.persona = persona
                                idioma.save()
                    elif len(form3.cleaned_data) >= 1:
                        for idi_padres in form3:
                            if idi_padres.cleaned_data:
                                idioma = idi_padres.save(commit=False)
                                idioma.persona = persona
                                idioma.save()

                    return HttpResponseRedirect(self.get_success_url())
                else:
                    print(form2.errors)
                    errors = {
                        'form':{'erros':form.errors, 'name':'Persona'},
                        'form2':{'erros':form2.errors, 'name':'PadresFamilia'},
                        'form3':{'erros':form3.errors, 'name':'IdiomaPersona'},
                    }
                    print(errors)
                    return self.render_to_response(self.get_context_data(form=form,
                        form2=form2,
                        form3=form3,
                    ))
        except IntegrityError:
            return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

class PadFamEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    template_name = "municipalizacion/padfam_edit.html"
    success_url = reverse_lazy("municipalizacion:padfam_list")
    model = PadresFamilia
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = PadFamForm
    third_form_class = IdPerForm
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.second_form_class

        return context

    def post(self, request, *args, **kwargs):
        padfam = self.get_object()
        persona = padfam.persona
        idioma_padres = IdiomaPersona.objects.filter(persona=persona)

        form = self.form_class(request.POST, request.FILES, instance = persona)
        form2 = self.second_form_class(request.POST, instance = padfam)

        with transaction.atomic():
            for idi_padres in idioma_padres:
                form3 = self.third_form_class(request.POST, instance=idi_padres, prefix='idiomas_padres')
                if form3.is_valid():
                    form3.save()
            if form.is_valid() and form2.is_valid():
                form.save()
                form2.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

    def get(self, request, *args, **kwargs):
        padfam = self.get_object()
        persona = padfam.persona

        try:
            form_idioma_padres = formset_factory(IdPerForm, extra=0)
            list_idpadres= []
            idioma_padres = IdiomaPersona.objects.filter(persona=persona)
            for idpadres in idioma_padres:
                list_idpadres.append({
                    'idioma': idpadres.idioma.id,
                    'estado_ip': idpadres.estado_ip
                })
            formset_idpadres = form_idioma_padres(initial=list_idpadres, prefix='idiomas_padres')
        except:
            print('Ocurrió un error')
            return HttpResponseRedirect(self.success_url)

        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = padfam)
        if 'form3' not in context:
            context['form3'] = formset_idpadres
        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)

class PadFamDetail(IsCoordinadorMunicipalMixin, generic.DetailView):
    template_name = "municipalizacion/padfam_detail.html"
    model = PadresFamilia

    def get_idioma(self, persona):
        return IdiomaPersona.objects.filter(persona=persona)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        padfam = self.get_object()
        persona = padfam.persona
        context['item'] = padfam
        context['persona'] = persona
        context['idioma_persona'] = self.get_idioma(persona)
        return context


class PadFamDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = PadresFamilia
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:padfam_list")
