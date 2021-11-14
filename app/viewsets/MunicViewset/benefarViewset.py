from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ImproperlyConfigured
from app.viewsets.users.CoordinadorMunicipal.mixin import IsCoordinadorMunicipalMixin
from app.viewsets.users.mixins.CooMunicipalYEquipoMunicipal import RolesCooMunicipalEquipoMunicipalMixin
from django.db.models import F
from app.models import BeneficiadoArea, Area
from app.forms import BenefArForm, AreaForm

def beneficiado_areaView(request, pk):
    queryset = BeneficiadoArea.objects.all().filter(area__id=pk)
    print("CONSULTA AREA", queriset)
    context = {
        'beneficiados_area':queryset,
    }
    return render(request, 'municipalizacion/benefar_list.html', context)

class BenefArView(IsCoordinadorMunicipalMixin, generic.ListView):
    model = BeneficiadoArea
    template_name = 'municipalizacion/benefar_list.html'
    context_object_name = 'obj'
    login_url = 'app:login'

    def get_queryset(self):
        qs = BeneficiadoArea.objects.all()
        area_id = self.request.GET.get("nombre_area")
        if area_id:
            qs = qs.filter(area__id=area_id)
        print(qs)
        return qs

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['areas'] = Area.objects.filter(estado_area=True)
        id_area = None
        if self.request.GET.get("nombre_area"):
            id_area = Area.objects.filter(id=int(self.request.GET.get("nombre_area"))).first()
        context['id_area'] = id_area
        return context

class BenefArNew(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = BeneficiadoArea
    template_name = 'municipalizacion/benefar_form.html'
    context_object_name = "obj"
    form_class = BenefArForm
    success_url = reverse_lazy("municipalizacion:benefar_list")
    login_url = 'app:login'
    id_area = ''

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
                return ["equipoMunicipal/benefar_form.html"]
            else:
                return [self.template_name]

    def get_queryset(self):
        return Area.objects.all()

    def get_object(self):
        area_id = self.kwargs.get('pk')
        qs = None
        if area_id:
            qs = self.get_queryset().filter(id=area_id).first()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_area'] = self.get_object().id if self.get_object() else ''
        context['areas'] = Area.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        self.id_area = self.get_object()
        super().post(request, *args, **kwargs)

    def form_valid(self, form):
        if form.is_valid():
            if self.id_area:
                area_benef = BeneficiadoArea(**form.cleaned_data, area=self.id_area)
                area_benef.save()
                return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class Area_beneficiado(RolesCooMunicipalEquipoMunicipalMixin, generic.CreateView):
    model = BeneficiadoArea
    template_name = 'municipalizacion/area_beneficiado.html'
    context_object_name = "obj"
    form_class = BenefArForm
    success_url = reverse_lazy("municipalizacion:benefar_por_area")
    login_url = 'app:login'
    id_areaben = ''

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
                return ["equipoMunicipal/benefar_form.html"]
            else:
                return [self.template_name]

    def get_queryset(self):
        return Area.objects.all()

    def get_object(self):
        area_id = self.kwargs.get('id_area')
        qs = None
        if area_id:
            qs = self.get_queryset().filter(id=area_id).first()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_areaben'] = self.get_object().id if self.get_object() else ''
        context['areas'] = Area.objects.all()
        return context

    def form_valid(self, form):
        if form.is_valid():
            self.id_areaben = self.get_object()
            if self.id_areaben:
                asignacion = BeneficiadoArea(**form.cleaned_data, area=self.id_areaben)
                asignacion.save()
                return redirect("municipalizacion:benefar_por_area")
            else:
                return self.render_to_response(self.get_context_data(form=form))


class BenefArEdit(IsCoordinadorMunicipalMixin, generic.UpdateView):
    model = BeneficiadoArea
    template_name = "municipalizacion/benefar_form.html"
    context_object_name = "obj"
    form_class = BenefArForm
    success_url = reverse_lazy("municipalizacion:benefar_list")
    login_url = 'app:login'

class BenefArDel(IsCoordinadorMunicipalMixin, generic.DeleteView):
    model = BeneficiadoArea
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:benefar_list")
