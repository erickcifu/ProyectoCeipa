from django.http.response import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from app.forms.educacionForms.personalForms import MaestroCentroForm
from django.contrib.auth.models import User
from django.db.models import F
from django.shortcuts import redirect
from app.models.educacion_model.centro_educativo import centro_educativo
from app.models.educacion_model.centropersonaModel import Centropersona
from .mixin import IsDirectorCentroMixin

class CrearMaestroDeCadaCentro(IsDirectorCentroMixin,generic.CreateView):
    model = User
    form_class = MaestroCentroForm
    template_name = 'directorCentro/crearMaestro.html'
    success_url = reverse_lazy('educacion:listado_personal_centro')

    def get_object(self):
        user = self.request.user
        return centro_educativo.objects.filter(c_educativo__personal__perfile = user.user_profile).first()

    def form_valid(self, form):
        user,personal = form.save()
        centro = self.get_object()
        asignacion = Centropersona(personal = personal, centro_Educativo=centro)
        asignacion.save()
        print('se ha creado correctamente')
        return redirect('educacion:listado_personal_centro')