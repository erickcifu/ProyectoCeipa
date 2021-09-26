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

    path('', viewsets.Home.as_view(), name = 'home'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/login.html'), name = 'logout'),
]
