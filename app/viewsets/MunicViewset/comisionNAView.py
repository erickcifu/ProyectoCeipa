from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError, transaction
from django.forms import formset_factory

from app.models import ComisionNA, Persona, IdiomaPersona
from app.forms import Comision_NAForm, PersonaForm, IdPerForm
from app.models.educacion_model.idioma import idioma

class ComisionNAView(LoginRequiredMixin, generic.ListView):
    model = ComisionNA
    template_name = 'municipalizacion/comisionNA_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class ComisionNANew(LoginRequiredMixin, generic.CreateView):
    model = ComisionNA
    template_name = 'municipalizacion/comisionNA_form.html'
    context_object_name = "obj"
    form_class = PersonaForm
    second_form_class = Comision_NAForm
    third_form_class = formset_factory(IdPerForm, extra=1)
    success_url = reverse_lazy("municipalizacion:comisionNA_list")
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super(ComisionNANew, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.third_form_class(prefix = 'idiomas_na')
        return context

    def get_object(self, request, pk, *args, **kwargs):
        return get_object_or_404(ComisionNA, pk=self.kwargs.get('pk'))

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                self.object = self.get_object
                form = self.form_class(request.POST, request.FILES)
                form2 = self.second_form_class(request.POST)
                form3 = self.third_form_class(request.POST, prefix = 'idiomas_na')
                if form.is_valid() and form2.is_valid() and form3.is_valid():
                    persona = form.save()
                    comision_na = form2.save(commit=False)
                    comision_na.persona_cna = persona
                    comision_na.save()
                    for form_idiomas in form3:
                        idioma = form_idiomas.save(commit=False)
                        idioma.persona = persona
                        idioma.save()
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))
        except IntegrityError:
            return HttpResponseRedirect("ERROR: No se puede registrar al participante")

class ComisionNAEdit(LoginRequiredMixin, generic.UpdateView):
    model = ComisionNA
    template_name = "municipalizacion/comisionNA_edit.html"
    form_class = PersonaForm
    second_form_class = Comision_NAForm
    third_form_class = IdPerForm
    success_url = reverse_lazy("municipalizacion:comisionNA_list")
    login_url = 'app:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_na'] = self.second_form_class
        context['obj'] = ''
        return context

    def post(self, request, *args, **kwargs):
        comna = self.get_object()
        persona_cna = comna.persona_cna
        idioma = IdiomaPersona.objects.filter(persona=persona_cna)
        form = self.form_class(request.POST, instance = persona_cna)
        form2 = self.second_form_class(request.POST, instance = comna)

        with transaction.atomic():
            for idioma_comi in idioma:
                form3 = self.third_form_class(request.POST, instance=idioma_comi, prefix='idiomas')
                if form3.is_valid():
                    form3.save()
            if form.is_valid() and form2.is_valid():
                form.save()
                form2.save()
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))

    def get(self, request, *args, **kwargs):
        comna = self.get_object()
        persona_cna = comna.persona_cna

        try:
            formidiomas = formset_factory(IdPerForm, extra=0)
            list_idcomi = []
            print(list_idcomi)
            idioma_comi = IdiomaPersona.objects.filter(persona=persona_cna)
            print('Si filtra')
            for i in idioma_comi:
                list_idcomi.append({
                    'idioma': i.idioma.id,
                    'estado_ip': i.estado_ip
                })
            print('List: ', list_idcomi)
            formsetidcomi = formidiomas(initial=list_idcomi, prefix='idiomas')
        except:
            print('Ocurrió un error')
            return HttpResponseRedirect(self.success_url)
        context = {}
        if 'form' not in context:
            context['form'] = self.form_class(instance = persona_cna)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance = comna)
        if 'form3' not in context:
            context['form3'] = formsetidcomi
        context['obj'] = ''
        context['persona'] = self.get_object()

        return render(request, self.template_name, context)

class ComisionNADetail(LoginRequiredMixin, generic.DetailView):
    template_name = "municipalizacion/comisionNA_detail.html"
    model = ComisionNA

    def get_idioma_na(self, persona_na):
        return IdiomaPersona.objects.filter(persona=persona_na)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comna = self.get_object()
        persona_na = comna.persona_cna
        context['item'] = comna
        context['persona_na'] = persona_na
        context['id_per_na'] = self.get_idioma_na(persona_na)
        return context
        
class ComisionNADel(LoginRequiredMixin, generic.DeleteView):
    model = ComisionNA
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:comisionNA_list")
