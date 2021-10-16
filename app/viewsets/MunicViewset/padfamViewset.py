from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.db import IntegrityError, transaction

from app.models import PadresFamilia, IdiomaPersona, Persona
from app.forms import PadFamForm, IdPerForm, PersonaForm

class PadFamView(LoginRequiredMixin, generic.ListView):
    model = PadresFamilia
    template_name = 'municipalizacion/padfam_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class PadFamNew(LoginRequiredMixin, generic.CreateView):
    model = PadresFamilia
    template_name = 'municipalizacion/padfam_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = PadFamForm
    third_form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:padfam_list")
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super(PadFamNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(PadresFamilia, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                self.object = self.get_object
                form = self.form_class(request.POST)
                form2 = self.second_form_class(request.POST)
                form3 = self.third_form_class(request.POST)

                if form.is_valid() and form2.is_valid() and form3.is_valid():
                    persona = form.save()
                    padfam = form2.save(commit=False)
                    padfam.persona = persona
                    padfam.save()
                    idioma = form3.save(commit=False)
                    idioma.persona = persona
                    idioma.save()
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))
        except IntegrityError:
            handle_exception()

class PadFamEdit(LoginRequiredMixin, generic.UpdateView):
    model = PadresFamilia
    template_name = "municipalizacion/padfam_form.html"
    context_object_name = "obj"
    form_class = PadFamForm
    success_url = reverse_lazy("municipalizacion:padfam_list")
    login_url = 'app:login'

class PadFamDel(LoginRequiredMixin, generic.DeleteView):
    model = PadresFamilia
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:padfam_list")
