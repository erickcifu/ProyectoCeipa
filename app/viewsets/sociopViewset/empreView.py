from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from app.models import Emprendimiento, PersonaBasica
from app.forms import EmprenForm

class EmprenView(LoginRequiredMixin, generic.ListView):
    model = Emprendimiento
    template_name = 'socioproductivo/Emprendimiento_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

class EmprenNew(LoginRequiredMixin, generic.CreateView):
    model = Emprendimiento
    template_name = "socioproductivo/Emprendimiento_form.html"
    context_object_name = "obj"
    form_class = EmprenForm
    success_url = reverse_lazy("socioproductivo:emprend_list")
    login_url = 'app:login'
    id_persona = ''

    def get_queryset(self):
        return PersonaBasica.objects.all()

    def get_object(self):
        persona_id = self.kwargs.get('pk')
        qs = None
        if persona_id:
            qs = self.get_queryset().filter(id=persona_id).first()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_persona'] = self.get_object().id if self.get_object() else ''
        context['personas'] = PersonaBasica.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        self.id_persona = self.get_object()
        super().post(request, *args, **kwargs)
        
    def form_valid(self, form):
        if form.is_valid():
            if self.id_persona:
                emprendimiento_persona = Emprendimiento(**form.cleaned_data, persona=self.id_persona)
                emprendimiento_persona.save()
                print('se guardó', emprendimiento_persona)
                return HttpResponseRedirect(self.success_url)
            else:
                return self.render_to_response(self.get_context_data(form=form))

class EmprenEdit(LoginRequiredMixin, generic.UpdateView):
    model = Emprendimiento
    template_name = "socioproductivo/Emprendimiento_form.html"
    context_object_name = "obj"
    form_class = EmprenForm
    success_url = reverse_lazy("socioproductivo:emprend_list")
    login_url = 'app:login'

class EmprenDel(LoginRequiredMixin, generic.DeleteView):
    model = Emprendimiento
    template_name = "socioproductivo/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("socioproductivo:emprend_list")
