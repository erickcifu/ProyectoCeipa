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
from django.db import IntegrityError, transaction

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
    third_form_class = IdPerForm
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
            context['form3'] = self.third_form_class(self.request.GET)
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
                form = self.form_class(request.POST)
                form2 = self.second_form_class(request.POST)
                form3 = self.third_form_class(request.POST)
                form4 = self.four_form_class(request.POST)
                if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
                    persona = form.save()
                    beneficiado = form2.save(commit=False)
                    beneficiado.persona = persona
                    beneficiado.tutor = form4.save()
                    beneficiado.save()
                    idioma = form3.save(commit=False)
                    idioma.persona = persona
                    idioma.save()
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4))
        except IntegrityError:
            handle_exception()

class BenEdit(LoginRequiredMixin, generic.UpdateView):
    template_name = "municipalizacion/beneficiado_form.html"
    success_url = reverse_lazy("municipalizacion:ben_list")
    context_object_name = "obj"
    model = Beneficiado
    form_class = PersonaForm
    second_form_class = BenForm
    third_form_class = IdPerForm
    four_form_class = TutorMuniForm
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.second_form_class

        return context

    def post(self, request, *args, **kwargs):
        beneficiado = self.get_object()
        persona = beneficiado.persona
        idioma = persona.I_persona.first()
        tutor = beneficiado.tutor

        form = self.form_class(request.POST, instance = persona)
        form2 = self.second_form_class(request.POST, instance = beneficiado)
        form3 = self.third_form_class(request.POST, instance = idioma )
        form4 = self.four_form_class(request.POST, instance = tutor )

        with transaction.atomic():
            if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
                form.save()
                form2.save()
                form3.save()
                form4.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3, form4=form4))

    def get(self, request, *args, **kwargs):
        beneficiado = self.get_object()
        persona = beneficiado.persona
        idioma = persona.I_persona.first()
        tutor = beneficiado.tutor

        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = beneficiado)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(instance = idioma)
        if 'form4' not in context:
            context['form4'] = self.four_form_class(instance = tutor)

        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)

class BenDel(LoginRequiredMixin, generic.DeleteView):
    model = Beneficiado
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:ben_list")
