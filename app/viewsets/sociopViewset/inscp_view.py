from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Inscripcionp, PersonaBasica, Taller
from app.forms import InscpForm, InscTallerForm

class InscpView(LoginRequiredMixin, generic.ListView):
    model = Inscripcionp
    template_name = 'socioproductivo/inscp_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class InscpNew(LoginRequiredMixin, generic.CreateView):
    model = Inscripcionp
    template_name = "socioproductivo/inscp_form.html"
    context_object_name = "obj"
    form_class = InscpForm
    success_url = reverse_lazy("socioproductivo:inscp_list")
    login_url = 'app:login'

class InscpEdit(LoginRequiredMixin, generic.UpdateView):
    model = Inscripcionp
    template_name = "socioproductivo/inscp_form.html"
    context_object_name = "obj"
    form_class = InscpForm
    success_url = reverse_lazy("socioproductivo:inscp_list")
    login_url = 'app:login'

class InscpDel(LoginRequiredMixin, generic.DeleteView):
    model = Inscripcionp
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:inscp_list")

class InscribirParticipanteTaller(LoginRequiredMixin, generic.CreateView):
    model = Inscripcionp
    template_name = "socioproductivo/inscp_participante.html"
    context_object_name = "obj"
    form_class = InscTallerForm
    success_url = reverse_lazy("socioproductivo:part_taller")
    login_url = 'app:login'

    def get_queryset(self):
        return Taller.objects.all()

    def get_object(self):
        id_taller = self.kwargs.get('pk')
        qs = None
        if id_taller:
            qs = self.get_queryset().filter(id=id_taller).first()
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_taller'] = self.get_object()
        context['talleres'] = Taller.objects.all()
        context['participantes'] = PersonaBasica.objects.exclude(ins_per__taller__id = self.get_object().id)
        return context

    def form_valid(self,form):
        if form.is_valid():
            taller_ins = self.get_object()
            if taller_ins:
                inscp = Inscripcionp.objects.create(**form.cleaned_data, taller=taller_ins)
                inscp.save()
            else:
                return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))
