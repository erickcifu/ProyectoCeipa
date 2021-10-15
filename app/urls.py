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

    path('curso/', viewsets.CursoView.as_view(), name='curso_list'),
    path('curso/new', viewsets.CursoNew.as_view(), name='curso_new'),
    path('curso/edit/<int:pk>', viewsets.CursoEdit.as_view(), name='curso_edit'),
    path('curso/delete/<int:pk>', viewsets.CursoDel.as_view(), name='curso_del'),

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

    path('tarea/', viewsets.TareaView.as_view(), name='tarea_list'),
    path('tarea/new', viewsets.TareaNew.as_view(), name='tarea_new'),
    path('tarea/edit/<int:pk>', viewsets.TareaEdit.as_view(), name='tarea_edit'),
    path('tarea/delete/<int:pk>', viewsets.TareaDel.as_view(), name='tarea_del'),

    path('grado/', viewsets.GradoView.as_view(), name='grado_list'),
    path('grado/new', viewsets.GradoNew.as_view(), name='grado_new'),
    path('grado/edit/<int:pk>', viewsets.GradoEdit.as_view(), name='grado_edit'),
    path('grado/delete/<int:pk>', viewsets.GradoDel.as_view(), name='grado_del'),

    path('religionalumno/', viewsets.Religion_alumnoView.as_view(), name='religionalum_list'),
    path('religionalumno/new', viewsets.Religion_alumnoNew.as_view(), name='religionalum_new'),
    path('religionalumno/edit/<int:pk>', viewsets.Religion_alumnoEdit.as_view(), name='religionalum_edit'),
    path('religionalumno/delete/<int:pk>', viewsets.Religion_alumnoDel.as_view(), name='religionalum_del'),

    path('techo/', viewsets.TechoView.as_view(), name='techo_list'),
    path('techo/new', viewsets.TechoNew.as_view(), name='techo_new'),
    path('techo/edit/<int:pk>', viewsets.TechoEdit.as_view(), name='techo_edit'),
    path('techo/delete/<int:pk>', viewsets.TechoDel.as_view(), name='techo_del'),

    path('pared/', viewsets.ParedView.as_view(), name='pared_list'),
    path('pared/new', viewsets.ParedNew.as_view(), name='pared_new'),
    path('pared/edit/<int:pk>', viewsets.ParedEdit.as_view(), name='pared_edit'),
    path('pared/delete/<int:pk>', viewsets.ParedDel.as_view(), name='pared_del'),

    path('etnia/', viewsets.EtniaView.as_view(), name='etnia_list'),
    path('etnia/new', viewsets.EtniaNew.as_view(), name='etnia_new'),
    path('etnia/edit/<int:pk>', viewsets.EtniaEdit.as_view(), name='etnia_edit'),
    path('etnia/delete/<int:pk>', viewsets.EtniaDel.as_view(), name='etnia_del'),

    path('servicioagua/', viewsets.ServiaguaView.as_view(), name='serviagua_list'),
    path('servicioagua/new', viewsets.ServiaguaNew.as_view(), name='serviagua_new'),
    path('servicioagua/edit/<int:pk>', viewsets.ServiaguaEdit.as_view(), name='serviagua_edit'),
    path('servicioagua/delete/<int:pk>', viewsets.ServiaguaDel.as_view(), name='serviagua_del'),

    path('conviviente/', viewsets.ConvivienteView.as_view(), name='conviviente_list'),
    path('conviviente/new', viewsets.ConvivienteNew.as_view(), name='conviviente_new'),
    path('conviviente/edit/<int:pk>', viewsets.ConvivienteEdit.as_view(), name='conviviente_edit'),
    path('conviviente/delete/<int:pk>', viewsets.ConvivienteDel.as_view(), name='conviviente_del'),

    path('tutor/', viewsets.TutorView.as_view(), name='tutor_list'),
    path('tutor/new', viewsets.TutorNew.as_view(), name='tutor_new'),
    path('tutor/edit/<int:pk>', viewsets.TutorEdit.as_view(), name='tutor_edit'),
    path('tutor/delete/<int:pk>', viewsets.TutorDel.as_view(), name='tutor_del'),

    path('alumno/', viewsets.AlumnoView.as_view(), name='alumno_list'),
    path('alumno/new', viewsets.AlumnoNew.as_view(), name='alumno_new'),
    path('alumno/edit/<int:pk>', viewsets.AlumnoEdit.as_view(), name='alumno_edit'),
    path('alumno/delete/<int:pk>', viewsets.AlumnoDel.as_view(), name='alumno_del'),

    path('CentrtoPersona/', viewsets.CentPerView.as_view(), name='centper_list'),
    path('CentrtoPersona/new', viewsets.CentPerNew.as_view(), name='centper_new'),
    path('CentrtoPersona/edit/<int:pk>', viewsets.CentPerEdit.as_view(), name='centper_edit'),
    path('CentrtoPersona/delete/<int:pk>', viewsets.CentPerDel.as_view(), name='centper_del'),

    path('EstudiosAnteriores/', viewsets.EstAntView.as_view(), name='estant_list'),
    path('EstudiosAnteriores/new', viewsets.EstAntNew.as_view(), name='estant_new'),
    path('EstudiosAnteriores/edit/<int:pk>', viewsets.EstAntEdit.as_view(), name='estant_edit'),
    path('EstudiosAnteriores/delete/<int:pk>', viewsets.EstAntDel.as_view(), name='estant_del'),

    path('CicloGrado/', viewsets.CGView.as_view(), name='cg_list'),
    path('CicloGrado/new', viewsets.CGNew.as_view(), name='cg_new'),
    path('CicloGrado/edit/<int:pk>', viewsets.CGEdit.as_view(), name='cg_edit'),
    path('CicloGrado/delete/<int:pk>', viewsets.CGDel.as_view(), name='cg_del'),

    path('CicloGradoCurso/', viewsets.CGCView.as_view(), name='cgc_list'),
    path('CicloGradoCurso/new', viewsets.CGCNew.as_view(), name='cgc_new'),
    path('CicloGradoCurso/edit/<int:pk>', viewsets.CGCEdit.as_view(), name='cgc_edit'),
    path('CicloGradoCurso/delete/<int:pk>', viewsets.CGCDel.as_view(), name='cgc_del'),

    path('inscripsion/', viewsets.InsView.as_view(), name='ins_list'),
    path('inscripsion/new', viewsets.InsNew.as_view(), name='ins_new'),
    path('inscripsion/edit/<int:pk>', viewsets.InsEdit.as_view(), name='ins_edit'),
    path('inscripsion/delete/<int:pk>', viewsets.InsDel.as_view(), name='ins_del'),

    path('Vivienda/', viewsets.VivView.as_view(), name='viv_list'),
    path('Vivienda/new', viewsets.VivNew.as_view(), name='viv_new'),
    path('Vivienda/edit/<int:pk>', viewsets.VivEdit.as_view(), name='viv_edit'),
    path('Vivienda/delete/<int:pk>', viewsets.VivDel.as_view(), name='viv_del'),
    #Municipalizacion

    path('area/', viewsets.AreaView.as_view(), name='area_list'),
    path('area/new', viewsets.AreaNew.as_view(), name='area_new'),
    path('area/edit/<int:pk>', viewsets.AreaEdit.as_view(), name='area_edit'),
    path('area/delete/<int:pk>', viewsets.AreaDel.as_view(), name='area_del'),

    path('cursogrupo/', viewsets.CarGView.as_view(), name='carg_list'),
    path('cursogrupo/new', viewsets.CarGNew.as_view(), name='carg_new'),
    path('cursogrupo/edit/<int:pk>', viewsets.CarGEdit.as_view(), name='carg_edit'),
    path('cursogrupo/delete/<int:pk>', viewsets.CarGDel.as_view(), name='carg_del'),

    path('idiomaPersona/', viewsets.IdPerView.as_view(), name='idper_list'),
    path('idiomaPersona/new', viewsets.IdPerNew.as_view(), name='idper_new'),
    path('idiomaPersona/edit/<int:pk>', viewsets.IdPerEdit.as_view(), name='idper_edit'),
    path('idiomaPersona/delete/<int:pk>', viewsets.IdPerDel.as_view(), name='idper_del'),

    path('persona/', viewsets.PerView.as_view(), name='per_list'),
    path('persona/new', viewsets.PerNew.as_view(), name='per_new'),
    path('persona/edit/<int:pk>', viewsets.PerEdit.as_view(), name='per_edit'),
    path('persona/delete/<int:pk>', viewsets.PerDel.as_view(), name='per_del'),

    path('beneficiado/', viewsets.BenView.as_view(), name='ben_list'),
    path('beneficiado/new', viewsets.BenNew.as_view(), name='ben_new'),
    path('beneficiado/edit/<int:pk>', viewsets.BenEdit.as_view(), name='ben_edit'),
    path('beneficiado/delete/<int:pk>', viewsets.BenDel.as_view(), name='ben_del'),

    path('maestro/', viewsets.MaesView.as_view(), name='maes_list'),
    path('maestro/new', viewsets.MaesNew.as_view(), name='maes_new'),
    path('maestro/edit/<int:pk>', viewsets.MaesEdit.as_view(), name='maes_edit'),
    path('maestro/delete/<int:pk>', viewsets.MaesDel.as_view(), name='maes_del'),

    path('profesion/', viewsets.ProfView.as_view(), name='prof_list'),
    path('profesion/new', viewsets.ProfNew.as_view(), name='prof_new'),
    path('profesion/edit/<int:pk>', viewsets.ProfEdit.as_view(), name='prof_edit'),
    path('profesion/delete/<int:pk>', viewsets.ProfDel.as_view(), name='prof_del'),

    path('discapacidad/', viewsets.DiscView.as_view(), name='disc_list'),
    path('discapacidad/new', viewsets.DiscNew.as_view(), name='disc_new'),
    path('discapacidad/edit/<int:pk>', viewsets.DiscEdit.as_view(), name='disc_edit'),
    path('discapacidad/delete/<int:pk>', viewsets.DiscDel.as_view(), name='disc_del'),

    path('cargo/', viewsets.CarView.as_view(), name='cargo_list'),
    path('cargo/new', viewsets.CarNew.as_view(), name='cargo_new'),
    path('cargo/edit/<int:pk>', viewsets.CarEdit.as_view(), name='cargo_edit'),
    path('cargo/delete/<int:pk>', viewsets.CarDel.as_view(), name='cargo_del'),

    path('comision/', viewsets.ComView.as_view(), name='com_list'),
    path('comision/new', viewsets.ComNew.as_view(), name='com_new'),
    path('comision/edit/<int:pk>', viewsets.ComEdit.as_view(), name='com_edit'),
    path('comision/delete/<int:pk>', viewsets.ComDel.as_view(), name='com_del'),

    path('establecimiento/', viewsets.EstablecimientoView.as_view(), name='establecimiento_list'),
    path('establecimiento/new', viewsets.EstablecimientoNew.as_view(), name='establecimiento_new'),
    path('establecimiento/edit/<int:pk>', viewsets.EstablecimientoEdit.as_view(), name='establecimiento_edit'),
    path('establecimiento/delete/<int:pk>', viewsets.EstablecimientoDel.as_view(), name='establecimiento_del'),

    path('partidopolitico/', viewsets.PartidoPoliticView.as_view(), name='partidopolitic_list'),
    path('partidopolitico/new', viewsets.PartidoPoliticNew.as_view(), name='partidopolitic_new'),
    path('partidopolitico/edit/<int:pk>', viewsets.PartidoPoliticEdit.as_view(), name='partidopolitic_edit'),
    path('partidopolitico/delete/<int:pk>', viewsets.PartidoPoliticDel.as_view(), name='partidopolitic_del'),

    path('mediodecomunicacion/', viewsets.MedioComuniView.as_view(), name='mediocomu_list'),
    path('mediodecomunicacion/new', viewsets.MedioComuniNew.as_view(), name='mediocomu_new'),
    path('mediodecomunicacion/edit/<int:pk>', viewsets.MedioComuniEdit.as_view(), name='mediocomu_edit'),
    path('mediodecomunicacion/delete/<int:pk>', viewsets.MedioComuniDel.as_view(), name='mediocomu_del'),

    path('ausenciabeneficiado/', viewsets.AusenBeneficiadoView.as_view(), name='ausbenefi_list'),
    path('ausenciabeneficiado/new', viewsets.AusenBeneficiadoNew.as_view(), name='ausbenefi_new'),
    path('ausenciabeneficiado/edit/<int:pk>', viewsets.AusenBeneficiadoEdit.as_view(), name='ausbenefi_edit'),
    path('ausenciabeneficiado/delete/<int:pk>', viewsets.AusenBeneficiadoDel.as_view(), name='ausbenefi_del'),

    path('tutormuni/', viewsets.TutorMuniView.as_view(), name='tutormuni_list'),
    path('tutormuni/new', viewsets.TutorMuniNew.as_view(), name='tutormuni_new'),
    path('tutormuni/edit/<int:pk>', viewsets.TutorMuniEdit.as_view(), name='tutormuni_edit'),
    path('tutormuni/delete/<int:pk>', viewsets.TutorMuniDel.as_view(), name='tutormuni_del'),

    path('lidercomunitario/', viewsets.LiderComunitarioMuniView.as_view(), name='lidercomuni_list'),
    path('lidercomunitario/new', viewsets.LiderComunitarioNew.as_view(), name='lidercomuni_new'),
    path('lidercomunitario/edit/<int:pk>', viewsets.LiderComunitarioEdit.as_view(), name='lidercomuni_edit'),
    path('lidercomunitario/delete/<int:pk>', viewsets.LiderComunitarioDel.as_view(), name='lidercomuni_del'),

    path('padecimientopersona/', viewsets.PadPerView.as_view(), name='padper_list'),
    path('padecimientopersona/new', viewsets.PadPerNew.as_view(), name='padper_new'),
    path('padecimientopersona/edit/<int:pk>', viewsets.PadPerEdit.as_view(), name='padper_edit'),
    path('padecimientopersona/delete/<int:pk>', viewsets.PadPerDel.as_view(), name='padper_del'),

    path('padresfamilia/', viewsets.PadFamView.as_view(), name='padfam_list'),
    path('padresfamilia/new', viewsets.PadFamNew.as_view(), name='padfam_new'),
    path('padresfamilia/edit/<int:pk>', viewsets.PadFamEdit.as_view(), name='padfam_edit'),
    path('padresfamilia/delete/<int:pk>', viewsets.PadFamDel.as_view(), name='padfam_del'),

    path('benefeciadoare/', viewsets.BenefArView.as_view(), name='benefar_list'),
    path('benefeciadoare/new', viewsets.BenefArNew.as_view(), name='benefar_new'),
    path('benefeciadoare/edit/<int:pk>', viewsets.BenefArEdit.as_view(), name='benefar_edit'),
    path('benefeciadoare/delete/<int:pk>', viewsets.BenefArDel.as_view(), name='benefar_del'),

    path('ausencia/', viewsets.AusView.as_view(), name='aus_list'),
    path('ausencia/new', viewsets.AusNew.as_view(), name='aus_new'),
    path('ausencia/edit/<int:pk>', viewsets.AusEdit.as_view(), name='aus_edit'),
    path('ausencia/delete/<int:pk>', viewsets.AusDel.as_view(), name='aus_del'),

    path('idioma_m/', viewsets.IdiomaMuniView.as_view(), name='idiomaMuni_list'),
    path('idioma_m/new', viewsets.IdiomaMuniNew.as_view(), name='idiomaMuni_new'),
    path('idioma_m/edit/<int:pk>', viewsets.IdiomaMuniEdit.as_view(), name='idiomaMuni_edit'),
    path('idioma_m/delete/<int:pk>', viewsets.IdiomaMuniDel.as_view(), name='idiomaMuni_del'),

    path('municipio_m/', viewsets.MunicView.as_view(), name='muni_list'),
    path('municipio_m/new', viewsets.MuniNew.as_view(), name='muni_new'),
    path('municipio_m/edit/<int:pk>', viewsets.MuniEdit.as_view(), name='muni_edit'),
    path('municipio_m/delete/<int:pk>', viewsets.MuniDel.as_view(), name='muni_del'),

    path('departamento_m/', viewsets.DeptoView.as_view(), name='depto_list'),
    path('departamento_m/new', viewsets.DeptoNew.as_view(), name='depto_new'),
    path('departamento_m/edit/<int:pk>', viewsets.DeptoEdit.as_view(), name='depto_edit'),
    path('departamento_m/delete/<int:pk>', viewsets.DeptoDel.as_view(), name='depto_del'),

    path('etnia_m/', viewsets.EtnMuniView.as_view(), name='etniamuni_list'),
    path('etnia_m/new', viewsets.EtniaMuniNew.as_view(), name='etniamuni_new'),
    path('etnia_m/edit/<int:pk>', viewsets.EtniaMuniEdit.as_view(), name='etniamuni_edit'),
    path('etnia_m/delete/<int:pk>', viewsets.EtniaMuniDel.as_view(), name='etniamuni_del'),

    path('estant_m/', viewsets.EstMuniView.as_view(), name='estmuni_list'),
    path('estant_m/new', viewsets.EstMuniNew.as_view(), name='estmuni_new'),
    path('estant_m/edit/<int:pk>', viewsets.EstMuniEdit.as_view(), name='estmuni_edit'),
    path('estant_m/delete/<int:pk>', viewsets.EstMuniDel.as_view(), name='estmuni_del'),

    path('padecimiento_m/', viewsets.PadMuniView.as_view(), name='padmuni_list'),
    path('padecimiento_m/new', viewsets.PadMuniNew.as_view(), name='padmuni_new'),
    path('padecimiento_m/edit/<int:pk>', viewsets.PadMuniEdit.as_view(), name='padmuni_edit'),
    path('padecimiento_m/delete/<int:pk>', viewsets.PadMuniDel.as_view(), name='padmuni_del'),

    path('genero_m/', viewsets.GeneroMuniView.as_view(), name='generomuni_list'),
    path('genero_m/new', viewsets.GeneroMuniNew.as_view(), name='generomuni_new'),
    path('genero_m/edit/<int:pk>', viewsets.GeneroMuniEdit.as_view(), name='generomuni_edit'),
    path('genero_m/delete/<int:pk>', viewsets.GeneroMuniDel.as_view(), name='generomuni_del'),

    path('ocupacion_m/', viewsets.OcupacionMuniView.as_view(), name='ocupmuni_list'),
    path('ocupacion_m/new', viewsets.OcupacionMuniNew.as_view(), name='ocupmuni_new'),
    path('ocupacion_m/edit/<int:pk>', viewsets.OcupacionMuniEdit.as_view(), name='ocupmuni_edit'),
    path('ocupacion_m/delete/<int:pk>', viewsets.OcupacionMuniDel.as_view(), name='ocupmuni_del'),

    path('corporacionmunicipal/', viewsets.CorpMuniView.as_view(), name='corpmuni_list'),
    path('corporacionmunicipal/new', viewsets.CorpMuniNew.as_view(), name='corpmuni_new'),
    path('corporacionmunicipal/edit/<int:pk>', viewsets.CorpMuniEdit.as_view(), name='corpmuni_edit'),
    path('corporacionmunicipal/delete/<int:pk>', viewsets.CorpMuniDel.as_view(), name='corpmuni_del'),

    path('', viewsets.Home.as_view(), name = 'home'),
    path('educacion/', viewsets.HomeEducacion.as_view(), name='educacion'),
    path('municipalizacion/', viewsets.HomeMunicipalizacion.as_view(), name='municipalizacion'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/login.html'), name = 'logout'),
]
