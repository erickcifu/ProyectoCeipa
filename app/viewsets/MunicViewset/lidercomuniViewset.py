from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.db import IntegrityError, transaction
from django.forms import formset_factory
from app.models import LiderComunitario, IdiomaPersona, Persona
from app.forms import LiderComuniMuniForm, IdPerForm, PersonaForm
from app.models.educacion_model.idioma import idioma

class LiderComunitarioMuniView(LoginRequiredMixin, generic.ListView):
    model = LiderComunitario
    template_name = 'municipalizacion/lidercomuni_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class LiderComunitarioNew(LoginRequiredMixin, generic.CreateView):
    model = LiderComunitario
    template_name = 'municipalizacion/lidercomuni_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = LiderComuniMuniForm
    third_form_class = formset_factory(IdPerForm, extra=1)
    success_url = reverse_lazy("municipalizacion:lidercomuni_list")
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super(LiderComunitarioNew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(prefix = 'idioma_lider')
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(LiderComunitario, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                self.object = self.get_object
                form = self.form_class(request.POST, request.FILES)
                form2 = self.second_form_class(request.POST)
                form3 = self.third_form_class(request.POST, prefix = 'idioma_lider')

                if form.is_valid() and form2.is_valid() and form3.is_valid():
                    persona = form.save()
                    lidercom = form2.save(commit=False)
                    lidercom.persona = persona
                    lidercom.save()
                    for idiom_lider in form3:
                        idioma = idiom_lider.save(commit=False)
                        idioma.persona = persona
                        idioma.save()
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))
        except IntegrityError:
            handle_exception()
class LiderComunitarioEdit(LoginRequiredMixin, generic.UpdateView):
    template_name = "municipalizacion/lidercomuni_edit.html"
    success_url = reverse_lazy("municipalizacion:lidercomuni_list")
    model = LiderComunitario
    form_class = PersonaForm
    second_form_class = LiderComuniMuniForm
    third_form_class = IdPerForm
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_lider'] = self.second_form_class
        context['obj'] = ''
        return context

    def post(self, request, *args, **kwargs):
        lidercom = self.get_object()
        persona_lider = lidercom.persona
        idioma = IdiomaPersona.objects.filter(persona=persona_lider)

        form = self.form_class(request.POST, instance = persona_lider)
        form2 = self.second_form_class(request.POST, instance = lidercom)

        with transaction.atomic():
            for idi_lider in idioma:
                form3 = self.third_form_class(request.POST, instance = idi_lider, prefix = 'idioma_lider')
                if form3.is_valid():
                    form3.save()
            if form.is_valid() and form2.is_valid():
                form.save()
                form2.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

    def get(self, request, *args, **kwargs):
        lidercom = self.get_object()
        persona_lider = lidercom.persona

        try:
            form_idlider = formset_factory(IdPerForm, extra=0)
            listado_idlider = []
            idi_lider = IdiomaPersona.objects.filter(persona=persona_lider)
            for i_lider in idi_lider:
                listado_idlider.append({
                    'idioma': i_lider.idioma.id,
                    'estado_ip': i_lider.estado_ip
                })
            formset_idlider = form_idlider(initial=listado_idlider, prefix = 'idioma_lider')
        except:
            print("Ocurrió un error")
            return HttpResponseRedirect(self.success_url)
        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona_lider)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = lidercom)
        if 'form3' not in context:
            context['form3'] = formset_idlider
        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)

class LiderComunitarioDetail(LoginRequiredMixin, generic.DetailView):
    template_name = "municipalizacion/lidercomuni_detail.html"
    model = LiderComunitario

    def get_idioma_lider(self, persona_lider):
        return IdiomaPersona.objects.filter(persona=persona_lider)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lidercom = self.get_object()
        persona_lider = lidercom.persona
        context['item'] = lidercom
        context['persona_lider'] = persona_lider
        context['idioma_lider'] = self.get_idioma_lider(persona_lider)
        return context

class LiderComunitarioDel(LoginRequiredMixin, generic.DeleteView):
    model = LiderComunitario
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:lidercomuni_list")
