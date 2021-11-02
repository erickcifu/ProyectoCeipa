from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.forms import inlineformset_factory

from django.db.models import F
from app.models import BeneficiadoArea, Area, Beneficiado, ProgramaC
from app.forms import BenefArForm, AreaForm

def beneficiado_areaView(request, pk):
    queryset = BeneficiadoArea.objects.all().filter(area__id=pk)
    print("CONSULTA AREA", queriset)
    context = {
        'beneficiados_area':queryset,
    }
    return render(request, 'municipalizacion/benefar_list.html', context)

class BenefArView(LoginRequiredMixin, generic.ListView):
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

class BenefArNew(LoginRequiredMixin, generic.CreateView):
    model = BeneficiadoArea
    template_name = 'municipalizacion/benefar_form.html'
    context_object_name = "obj"
    form_class = BenefArForm
    success_url = reverse_lazy("municipalizacion:benefar_list")
    login_url = 'app:login'

    def get_areas(self):
        id_area = self.kwargs.get('id_area')
        if id_area:
            return Area.objects.filter(id=int(id_area)).first()
        return None

        def get(self, request, *args, **kwargs):
            id_area = self.get_areas()
            context={}
            context['id_area'] = id_area
            context['beneficiado'] = Beneficiado.objects.filter(estado_beneficiado=True).exclude(ba_benef__area_id = id_area.id)
            return render(request, self.template_name, context)

        def post(self, request, *args, **kwargs):
            id_area = self.get_areas()
            beneficiados = self.request.POST.get('beneficiados')
            if beneficiados:
                fecha = datetime.now().strftime('%Y-%m-%d')
                BeneficiadoArea.objects.create(area=id_area, beneficiado_id=int(beneficiados), fecha=fecha)
                return redirect('municipalizacion/benefar_list.html', id_area=id_area.id)

class Area_beneficiado(LoginRequiredMixin, generic.ListView):
    model = BeneficiadoArea
    template_name = 'municipalizacion/area_beneficiado.html'
    context_object_name = "obj"
    form_class = BenefArForm
    success_url = reverse_lazy("municipalizacion:benefar_por_area")
    login_url = 'app:login'

    def get_object(self):
        id_area =  self.kwargs.get('pk')
        if id_area:
            return Area.objects.filter(id=int(id_area)).first()
        return None

    def post(self, request, *args, **kwargs):
        form = BenefArForm(request.POST)
        if form.is_valid():
            area_ben = self.get_object()
            if area_ben:
                fecha = datetime.now().strftime('%Y-%m-%d')
                observacion = ''
                BeneficiadoArea.objects.create(**form.cleaned_data, area=area_ben, fecha=fecha)
                return HttpResponseRedirect(self.success_url)
        return self.render_to_response(self.get_context_data(form=form))


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_area'] = self.get_object()
        context['areas'] = Area.objects.all()
        context['beneficiados'] = Beneficiado.objects.exclude(ba_benef__area__id = self.get_object().id)
        context['programa'] = ProgramaC.objects.all()
        return context

class BenefArEdit(LoginRequiredMixin, generic.UpdateView):
    model = BeneficiadoArea
    template_name = "municipalizacion/benefar_form.html"
    context_object_name = "obj"
    form_class = BenefArForm
    success_url = reverse_lazy("municipalizacion:benefar_list")
    login_url = 'app:login'

class BenefArDel(LoginRequiredMixin, generic.DeleteView):
    model = BeneficiadoArea
    template_name = "municipalizacion/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("municipalizacion:benefar_list")
