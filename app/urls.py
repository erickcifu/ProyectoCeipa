from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import  url
from app import viewsets
from django.contrib.auth import views as auth_views

#from app import viewsets

urlpatterns = [
    url(r"^app/token",obtain_auth_token, name="app-token"),
    path('api-auth/',include('rest_framework.urls')),

    path('parentesco/', viewsets.ParentescoView.as_view(), name='parentesco_list'),
    path('parentesco/new', viewsets.ParentescoNew.as_view(), name='parentesco_new'),
    path('parentesco/edit/<int:pk>', viewsets.ParentescoEdit.as_view(), name='parentesco_edit'),
    path('parentesco/delete/<int:pk>', viewsets.ParentescoDel.as_view(), name='parentesco_del'),

    path('departamento/', viewsets.DepartamentoView.as_view(), name='departamento_list'),
    path('departamento/new', viewsets.DepartamentoNew.as_view(), name='departamento_new'),
    path('departamento/edit/<int:pk>', viewsets.DepartamentoEdit.as_view(), name='departamento_edit'),
    path('departamento/delete/<int:pk>', viewsets.DepartamentoDel.as_view(), name='departamento_del'),

    path('municipio/', viewsets.MunicipioView.as_view(), name='municipio_list'),
    path('municipio/new', viewsets.MunicipioNew.as_view(), name='municipio_new'),
    path('municipio/edit/<int:pk>', viewsets.MunicipioEdit.as_view(), name='municipio_edit'),
    path('municipio/delete/<int:pk>', viewsets.MunicipioDel.as_view(), name='municipio_del'),

    path('seccion/', viewsets.SeccionView.as_view(), name='seccion_list'),
    path('seccion/new', viewsets.SeccionNew.as_view(), name='seccion_new'),
    path('seccion/edit/<int:pk>', viewsets.SeccionEdit.as_view(), name='seccion_edit'),
    path('seccion/delete/<int:pk>', viewsets.SeccionDel.as_view(), name='seccion_del'),

    path('Psicologico/', viewsets.PicoView.as_view(), name='psico_list'),
    path('Psicologico/new', viewsets.PsicoNew.as_view(), name='psico_new'),
    path('Psicologico/edit/<int:pk>', viewsets.PsicoEdit.as_view(), name='psico_edit'),
    path('Psicologico/delete/<int:pk>', viewsets.PsicoDel.as_view(), name='psico_del'),

    path('Categoria/', viewsets.CatView.as_view(), name='cat_list'),
    path('Categoria/new', viewsets.CatNew.as_view(), name='cat_new'),
    path('Categoria/edit/<int:pk>', viewsets.CatEdit.as_view(), name='cat_edit'),
    path('Categoria/delete/<int:pk>', viewsets.CatDel.as_view(), name='cat_del'),

    path('Tpiso/', viewsets.TpisoView.as_view(), name='tpiso_list'),
    path('Tpiso/new', viewsets.TpisoNew.as_view(), name='tpiso_new'),
    path('Tpiso/edit/<int:pk>', viewsets.TpisoEdit.as_view(), name='tpiso_edit'),
    path('Tpiso/delete/<int:pk>', viewsets.TpisoDel.as_view(), name='tpiso_del'),

    path('ocupacion/', viewsets.OcupView.as_view(), name='ocup_list'),
    path('ocupacion/new', viewsets.OcupNew.as_view(), name='ocup_new'),
    path('ocupacion/edit/<int:pk>', viewsets.OcupEdit.as_view(), name='ocup_edit'),
    path('ocupacion/delete/<int:pk>', viewsets.OcupDel.as_view(), name='ocup_del'),

    path('Padecimiento/', viewsets.PadView.as_view(), name='pade_list'),
    path('Padecimiento/new', viewsets.PadNew.as_view(), name='pad_new'),
    path('Padecimiento/edit/<int:pk>', viewsets.PadEdit.as_view(), name='pad_edit'),
    path('Padecimiento/delete/<int:pk>', viewsets.PadDel.as_view(), name='pad_del'),

    path('AlumnoPadecimiento/', viewsets.APadView.as_view(), name='apad_list'),
    path('AlumnoPadecimiento/new', viewsets.APadNew.as_view(), name='apad_new'),
    path('AlumnoPadecimiento/edit/<int:pk>', viewsets.APadEdit.as_view(), name='apad_edit'),
    path('AlumnoPadecimiento/delete/<int:pk>', viewsets.APadDel.as_view(), name='apad_del'),

    path('CentroEducativo/', viewsets.CenEdView.as_view(), name='centedu_list'),
    path('CentroEducativo/new', viewsets.CenEdNew.as_view(), name='centedu_new'),
    path('CentroEducativo/edit/<int:pk>', viewsets.CenEdEdit.as_view(), name='centedu_edit'),
    path('CentroEducativo/delete/<int:pk>', viewsets.CenEdDel.as_view(), name='centedu_del'),

    path('ciclo/', viewsets.CicloView.as_view(), name='ciclo_list'),
    path('ciclo/new', viewsets.CicloNew.as_view(), name='ciclo_new'),
    path('ciclo/edit/<int:pk>', viewsets.CicloEdit.as_view(), name='ciclo_edit'),
    path('ciclo/delete/<int:pk>', viewsets.CicloDel.as_view(), name='ciclo_del'),

    #path('curso/', viewsets.CursoView.as_view(), name='curso_list'),
    #path('curso/new', viewsets.CursoNew.as_view(), name='curso_new'),
    #path('curso/edit/<int:pk>', viewsets.CursoEdit.as_view(), name='curso_edit'),
    #path('curso/delete/<int:pk>', viewsets.CursoDel.as_view(), name='curso_del'),

    path('genero/', viewsets.GeneroView.as_view(), name='genero_list'),
    path('genero/new', viewsets.GeneroNew.as_view(), name='genero_new'),
    path('genero/edit/<int:pk>', viewsets.GeneroEdit.as_view(), name='genero_edit'),
    path('genero/delete/<int:pk>', viewsets.GeneroDel.as_view(), name='genero_del'),

    path('grados/', viewsets.GradosView.as_view(), name='grados_list'),
    path('grados/new', viewsets.GradosNew.as_view(), name='grados_new'),
    path('grados/edit/<int:pk>', viewsets.GradosEdit.as_view(), name='grados_edit'),
    path('grados/delete/<int:pk>', viewsets.GradosDel.as_view(), name='grados_del'),

    path('idioma/', viewsets.IdiomaView.as_view(), name='idioma_list'),
    path('idioma/new', viewsets.IdiomaNew.as_view(), name='idioma_new'),
    path('idioma/edit/<int:pk>', viewsets.IdiomaEdit.as_view(), name='idioma_edit'),
    path('idioma/delete/<int:pk>', viewsets.IdiomaDel.as_view(), name='idioma_del'),

    path('personal/', viewsets.PersonalView.as_view(), name='personal_list'),
    path('personal/new', viewsets.PersonalNew.as_view(), name='personal_new'),
    path('personal/edit/<int:pk>', viewsets.PersonalEdit.as_view(), name='personal_edit'),
    path('personal/delete/<int:pk>', viewsets.PersonalDel.as_view(), name='personal_del'),

    path('religion/', viewsets.ReligionView.as_view(), name='religion_list'),
    path('religion/new', viewsets.ReligionNew.as_view(), name='religion_new'),
    path('religion/edit/<int:pk>', viewsets.ReligionEdit.as_view(), name='religion_edit'),
    path('religion/delete/<int:pk>', viewsets.ReligionDel.as_view(), name='religion_del'),

    #path('tarea/', viewsets.TareaView.as_view(), name='tarea_list'),
    #path('tarea/new', viewsets.TareaNew.as_view(), name='tarea_new'),
    #path('tarea/edit/<int:pk>', viewsets.TareaEdit.as_view(), name='tarea_edit'),
    #path('tarea/delete/<int:pk>', viewsets.TareaDel.as_view(), name='tarea_del'),

    path('grado/', viewsets.GradoView.as_view(), name='grado_list'),
    path('grado/new', viewsets.GradoNew.as_view(), name='grado_new'),
    path('grado/edit/<int:pk>', viewsets.GradoEdit.as_view(), name='grado_edit'),
    path('grado/delete/<int:pk>', viewsets.GradoDel.as_view(), name='grado_del'),

    path('religionalumno/', viewsets.Religion_alumnoView.as_view(), name='religionalum_list'),
    path('religionalumno/new', viewsets.Religion_alumnoNew.as_view(), name='religionalum_new'),
    path('religionalumno/edit/<int:pk>', viewsets.Religion_alumnoEdit.as_view(), name='religionalum_edit'),
    path('religionalumno/delete/<int:pk>', viewsets.Religion_alumnoDel.as_view(), name='religionalum_del'),

    path('', viewsets.Home.as_view(), name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/login.html'), name = 'logout'),
]
