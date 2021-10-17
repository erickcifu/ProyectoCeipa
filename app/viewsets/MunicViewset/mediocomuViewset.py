from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from app.models import MedioComuni, Persona, IdiomaPersona
from app.forms import MedioComuniForm, PersonaForm,IdPerForm
from django.db import IntegrityError, transaction

class MedioComuniView(LoginRequiredMixin, generic.ListView):
    model = MedioComuni
    template_name = 'municipalizacion/mediocomu_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class MedioComuniNew(LoginRequiredMixin, generic.CreateView):
    model = MedioComuni
    template_name = 'municipalizacion/mediocomu_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = MedioComuniForm
    third_form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:mediocomu_list")
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super(MedioComuniNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(self.request.GET)
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(MedioComuni, pk=self.kwargs.get('pk'))

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
                    medio= form2.save(commit=False)
                    medio.persona = persona
                    medio.save()
                    idioma = form3.save(commit=False)
                    idioma.persona = persona
                    idioma.save()
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))
        except IntegrityError:
            handle_exception()

class MedioComuniEdit(LoginRequiredMixin, generic.UpdateView):
    model = MedioComuni
    template_name = "municipalizacion/mediocomu_form.html"
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = MedioComuniForm
    third_form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:mediocomu_list")
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.second_form_class

        return context

    def post(self, request, *args, **kwargs):
        medio = self.get_object()
        persona = medio.persona
        idioma = persona.I_persona.first()

        form = self.form_class(request.POST, instance = persona)
        form2 = self.second_form_class(request.POST, instance = medio)
        form3 = self.third_form_class(request.POST, instance = idioma )

        with transaction.atomic():
            if form.is_valid() and form2.is_valid() and form3.is_valid():
                form.save()
                form2.save()
                form3.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

    def get(self, request, *args, **kwargs):
        medio = self.get_object()
        persona = medio.persona
        idioma = persona.I_persona.first()

        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = medio)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(instance = idioma)
        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)

class MedioComuniDel(LoginRequiredMixin, generic.DeleteView):
    model = MedioComuni
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:mediocomu_list")
