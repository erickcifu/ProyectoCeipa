from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from app.models import Beneficiado, Persona, IdiomaPersona, TutorMuni
from app.forms import BenForm, PersonaForm, IdPerForm, TutorMuniForm
from django.forms import formset_factory
from django.db import IntegrityError, transaction
from app.models.educacion_model.idioma import idioma

class BenView(LoginRequiredMixin, generic.ListView):
    model = Beneficiado
    template_name = 'municipalizacion/beneficiado_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class BenNew(LoginRequiredMixin, generic.CreateView):
    model = Beneficiado
    template_name = 'municipalizacion/beneficiado_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = BenForm
    third_form_class = formset_factory(IdPerForm, extra=1)
    four_form_class = TutorMuniForm
    success_url = reverse_lazy("municipalizacion:ben_list")
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super(BenNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(prefix = 'idiomas')
        if 'form4' not in context:
            context['form4'] = self.four_form_class(self.request.GET)
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(Beneficiado, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                self.object = self.get_object
                form = self.form_class(request.POST, request.FILES)
                form2 = self.second_form_class(request.POST)
                form3 = self.third_form_class(request.POST, prefix = 'idiomas')
                form4 = self.four_form_class(request.POST)
                if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
                    persona = form.save()
                    beneficiado = form2.save(commit=False)
                    beneficiado.persona = persona
                    beneficiado.tutor = form4.save()
                    beneficiado.save()
                    for form_idiomas in form3:
                        idioma = form_idiomas.save(commit=False)
                        idioma.persona = persona
                        idioma.save()
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4))
        except IntegrityError:
            return HttpResponseRedirect("ERROR: No se puede registrar al participante")

class BenEdit(LoginRequiredMixin, generic.UpdateView):
    template_name = "municipalizacion/benefEdit.html"
    success_url = reverse_lazy("municipalizacion:ben_list")
    model = Beneficiado
    form_class = PersonaForm
    second_form_class = BenForm
    third_form_class = IdPerForm
    four_form_class = TutorMuniForm
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.second_form_class
        context['obj'] = ''
        return context

    def post(self, request, *args, **kwargs):
        beneficiado = self.get_object()
        persona = beneficiado.persona
        idioma = IdiomaPersona.objects.filter(persona=persona)
        tutor = beneficiado.tutor

        form = self.form_class(request.POST, request.FILES, instance = persona)
        form2 = self.second_form_class(request.POST, instance = beneficiado)
        form4 = self.four_form_class(request.POST, instance = tutor)

        with transaction.atomic():
            for idi in idioma:
                form3 = self.third_form_class(request.POST, instance = idi, prefix='idiomas')
                if form3.is_valid():
                    form3.save()
            if form.is_valid() and form2.is_valid() and form4.is_valid():
                form.save()
                form2.save()
                form4.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4))

    def get(self, request, *args, **kwargs):
        beneficiado = self.get_object()
        persona = beneficiado.persona
        tutor = beneficiado.tutor

        try:
            formidper = formset_factory(IdPerForm, extra=0)
            listadoIdper = []
            idiomas = IdiomaPersona.objects.filter(persona=persona)
            for i in idiomas:
                listadoIdper.append({
                    'idioma':i.idioma.id,
                    'estado_ip':i.estado_ip
                })
                print( listadoIdper)
            formsetidper = formidper(initial=listadoIdper, prefix='idiomas')
        except:
            print("error")
            return HttpResponseRedirect(self.success_url)
        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = beneficiado)
        if 'form3' not in context:
            context['form3'] = formsetidper
        if 'form4' not in context:
            context['form4'] = self.four_form_class(instance = tutor)

        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)

class BenDetail(LoginRequiredMixin, generic.DetailView):
    template_name = "municipalizacion/ben_detail.html"
    model = Beneficiado

    def get_idioma(self, persona):
        return IdiomaPersona.objects.filter(persona=persona)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        beneficiado = self.get_object()
        persona = beneficiado.persona
        context['item'] = beneficiado
        context['tutor'] = beneficiado.tutor
        context['persona'] = persona
        context['idioma_persona'] = self.get_idioma(persona)
        return context


class BenDel(LoginRequiredMixin, generic.DeleteView):
    model = Beneficiado
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:ben_list")
