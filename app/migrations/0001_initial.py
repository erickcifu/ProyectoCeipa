# Generated by Django 3.2.7 on 2021-10-03 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres_alumno', models.CharField(max_length=50)),
                ('cui', models.IntegerField()),
                ('apellidos_alumno', models.CharField(max_length=100, null=True)),
                ('codigo_mineduc', models.IntegerField()),
                ('estado_alumno', models.BooleanField(default=True)),
                ('fecha_nacimiento', models.DateField()),
                ('ingreso_familiar', models.FloatField()),
                ('direccion_alumno', models.CharField(max_length=80)),
                ('telefono', models.CharField(max_length=8)),
                ('fotografia', models.ImageField(blank=True, null=True, upload_to='ceipa')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_area', models.CharField(max_length=55)),
                ('estado_area', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ausencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iniciof', models.DateTimeField()),
                ('finf', models.DateTimeField()),
                ('razon', models.CharField(max_length=255)),
                ('estado_ausencia', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cargo', models.CharField(max_length=55)),
                ('estado_cargo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CargoGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cg', models.CharField(max_length=55)),
                ('estado_cg', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=55)),
                ('descripcion_categoria', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_categoria', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='centro_educativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_centro', models.CharField(max_length=100)),
                ('direccion_centro', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo_centro', models.CharField(max_length=50)),
                ('estado_centro', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField()),
                ('estado_ciclo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo_grado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_cg', models.BooleanField(default=True)),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cg_ciclo', to='app.ciclo')),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo_grado_curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_cgc', models.BooleanField(default=True)),
                ('ciclo_grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cgc_cg', to='app.ciclo_grado')),
            ],
        ),
        migrations.CreateModel(
            name='Comision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comision', models.CharField(max_length=55)),
                ('estado_comision', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_departamento', models.CharField(max_length=50)),
                ('estado_departamento', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Discapacidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_dis', models.CharField(max_length=55)),
                ('estado_dis', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_establecimiento', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=80)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='EstudiosAnt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_establecimiento', models.CharField(max_length=100)),
                ('repitente', models.BooleanField(default=True)),
                ('telefono', models.CharField(max_length=8)),
                ('estado_estudiosant', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='etnia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_etnia', models.CharField(max_length=50)),
                ('descripcion_etnia', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_etnia', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=50)),
                ('estado_genero', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GOrganizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_grupo', models.CharField(max_length=255)),
                ('estado_grupo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_grado', models.CharField(max_length=50)),
                ('descripcion_grado', models.CharField(blank=True, max_length=255, null=True)),
                ('estado_grado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='grados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_grados', models.CharField(max_length=50)),
                ('descripcion_grados', models.CharField(blank=True, max_length=255, null=True)),
                ('estado_grados', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_idioma', models.CharField(max_length=50)),
                ('descripcion_idioma', models.CharField(blank=True, max_length=255, null=True)),
                ('estado_idioma', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ins', models.CharField(max_length=255)),
                ('correo', models.EmailField(blank=True, max_length=55, null=True)),
                ('estado_ins', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_municipio', models.CharField(max_length=255)),
                ('estado_municipio', models.BooleanField(default=True)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='M_dep', to='app.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='ocupacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ocupacion', models.CharField(max_length=50)),
                ('descripcion_ocupacion', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_ocupacion', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Padecimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_padecimiento', models.CharField(max_length=205)),
                ('estado_padecimiento', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parentesco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_parentesco', models.CharField(max_length=50)),
                ('descripcion_parentesco', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_parentesco', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PartidoPolitic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_partido', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='personalEducativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('telefono_personal', models.CharField(blank=True, max_length=15, null=True)),
                ('email_personal', models.CharField(blank=True, max_length=50, null=True)),
                ('fechaNac_personal', models.DateTimeField()),
                ('direccion_personal', models.CharField(blank=True, max_length=255, null=True)),
                ('certificadoRenas_personal', models.BooleanField(default=False)),
                ('estado_personal', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_profesion', models.CharField(max_length=55)),
                ('estado_profesion', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProgramaC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_programa', models.CharField(max_length=255)),
                ('estado_programa', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_religion', models.CharField(max_length=50)),
                ('estado_religion', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_seccion', models.CharField(max_length=255)),
                ('estado_seccion', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio_Agua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio_agua', models.CharField(max_length=50)),
                ('descripcion_servicio_agua', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_agua', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_tarea', models.CharField(max_length=50)),
                ('descripcion_tarea', models.CharField(blank=True, max_length=255, null=True)),
                ('nota_tarea', models.FloatField()),
                ('fecha_entrega', models.DateTimeField()),
                ('estado_tarea', models.BooleanField(default=True)),
                ('ciclo_grado_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cgc_tarea', to='app.ciclo_grado_curso')),
                ('maestro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarea_maestro', to='app.personaleducativo')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_muro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_muro', models.CharField(max_length=50)),
                ('descripcion_muro', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_muro', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_piso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_piso', models.CharField(max_length=55)),
                ('descripcion_tipopiso', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_tipopiso', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_techo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_techo', models.CharField(max_length=50)),
                ('descripcion_techo', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_techo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TutorMuni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres_tutor', models.CharField(max_length=50)),
                ('apellidos_tutor', models.CharField(max_length=50, null=True)),
                ('DPI', models.IntegerField()),
                ('estado_tutor', models.BooleanField(default=True)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion_tutor', models.CharField(max_length=80)),
                ('telefono', models.CharField(max_length=8)),
                ('fotografia', models.ImageField(blank=True, null=True, upload_to='ceipa')),
            ],
        ),
        migrations.CreateModel(
            name='vivienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_personas', models.IntegerField()),
                ('cantidad_ambientes', models.IntegerField()),
                ('energia_electrica', models.BooleanField(default=False)),
                ('servicio_sanitario', models.BooleanField(default=False)),
                ('letrina', models.BooleanField(default=False)),
                ('estado_vivienda', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_vivienda', to='app.categoria')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estudiante_vivieda', to='app.alumno')),
                ('piso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='piso_vivienda', to='app.tipo_piso')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicio_vivienda', to='app.servicio_agua')),
                ('techo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='techo_vivienda', to='app.tipo_techo')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres_tutor', models.CharField(max_length=50)),
                ('apellidos_tutor', models.CharField(max_length=50, null=True)),
                ('DPI', models.IntegerField()),
                ('estado_tutor', models.BooleanField(default=True)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion_tutor', models.CharField(max_length=80)),
                ('telefono', models.CharField(max_length=8)),
                ('fotografia', models.ImageField(blank=True, null=True, upload_to='ceipa')),
                ('correo', models.EmailField(max_length=80)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ge_genero', to='app.genero')),
                ('muni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Mu_muni', to='app.municipio')),
                ('parentesco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pa_parentesco', to='app.parentesco')),
            ],
        ),
        migrations.CreateModel(
            name='tarea_alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_obtenida', models.FloatField()),
                ('observaciones', models.CharField(blank=True, max_length=255, null=True)),
                ('estado_entrega', models.BooleanField(default=False)),
                ('estado_tareaAlumno', models.BooleanField(default=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ta_alumno', to='app.alumno')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ta_tarea', to='app.tarea')),
            ],
        ),
        migrations.CreateModel(
            name='Religion_alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_iglesia', models.CharField(max_length=50)),
                ('estado_religionalumno', models.BooleanField(default=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='R_alumno', to='app.alumno')),
                ('religion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r_religion', to='app.religion')),
            ],
        ),
        migrations.CreateModel(
            name='psicologico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Analisis_psicologico', models.CharField(max_length=255)),
                ('tratamiento', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_Analisis', models.DateTimeField()),
                ('Entrevistador', models.CharField(blank=True, max_length=255, null=True)),
                ('estado_psicologico', models.BooleanField(default=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='A_alumno', to='app.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.CharField(max_length=50)),
                ('apellidos_persona', models.CharField(max_length=100, null=True)),
                ('fecha_nacimiento', models.DateField()),
                ('cui', models.IntegerField()),
                ('direccion_persona', models.CharField(max_length=80)),
                ('telefono', models.CharField(max_length=8)),
                ('telefonoc', models.CharField(max_length=8)),
                ('fotografia', models.ImageField(blank=True, null=True, upload_to='ceipa')),
                ('estado_persona', models.BooleanField(default=True)),
                ('disc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='T_disc', to='app.discapacidad')),
                ('estudios_anteriores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='P_estudios', to='app.estudiosant')),
                ('etni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='P_etnia', to='app.etnia')),
                ('gen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='P_genero', to='app.genero')),
                ('muni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='P_muni', to='app.municipio')),
            ],
        ),
        migrations.CreateModel(
            name='PadPer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicamentos', models.CharField(max_length=255)),
                ('observacion', models.CharField(max_length=255)),
                ('estado_padper', models.BooleanField(default=True)),
                ('padecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PP_padecimiento', to='app.padecimiento')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PP_persona', to='app.persona')),
            ],
        ),
        migrations.CreateModel(
            name='MedioComuni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_medio', models.CharField(max_length=50)),
                ('correo', models.EmailField(blank=True, max_length=55, null=True)),
                ('telefono', models.CharField(max_length=8)),
                ('estado', models.BooleanField(default=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='C_cargoM', to='app.cargo')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='P_personaM', to='app.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Maestro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_maestro', models.BooleanField(default=True)),
                ('cargogrup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='M_cargoG', to='app.gorganizado')),
                ('establecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='M_Est', to='app.establecimiento')),
                ('gruporg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='M_grupOrg', to='app.cargogrupo')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='M_persona', to='app.persona')),
            ],
        ),
        migrations.CreateModel(
            name='LiderComunitario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leer', models.BooleanField(default=True)),
                ('escribir', models.BooleanField(default=True)),
                ('vacuna_covid', models.BooleanField(default=True)),
                ('periodo', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.BooleanField(default=True)),
                ('cargo_grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='C_cargoGM', to='app.cargogrupo')),
                ('grupo_orga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='G_organizado', to='app.gorganizado')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='B_personaM', to='app.persona')),
                ('programa_c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='P_ceipa', to='app.programac')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_inscripcion', models.DateTimeField()),
                ('estado_incpripsion', models.BooleanField(default=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='A_alumnos', to='app.alumno')),
                ('centro_educativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='C_educativo', to='app.centro_educativo')),
                ('ciclo_grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ciclo_grado', to='app.ciclo_grado')),
            ],
        ),
        migrations.CreateModel(
            name='IdiomaPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_ip', models.BooleanField(default=True)),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='P_idioma', to='app.idioma')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='I_persona', to='app.persona')),
            ],
        ),
        migrations.AddField(
            model_name='estudiosant',
            name='grado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='E_grado', to='app.grados'),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_curso', models.CharField(max_length=100)),
                ('descripcion_curso', models.CharField(max_length=255)),
                ('estado_curso', models.BooleanField(default=True)),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='curso_grado', to='app.grado')),
            ],
        ),
        migrations.CreateModel(
            name='Conviviente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres_conviviente', models.CharField(max_length=50)),
                ('apellidos_conviviente', models.CharField(max_length=100, null=True)),
                ('estado_conviviente', models.BooleanField(default=True)),
                ('fecha_nacimiento', models.DateField()),
                ('parentesco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='P_parentesco', to='app.parentesco')),
                ('vivienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='V_vivienda', to='app.vivienda')),
            ],
        ),
        migrations.AddField(
            model_name='ciclo_grado_curso',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cgc_curso', to='app.curso'),
        ),
        migrations.AddField(
            model_name='ciclo_grado_curso',
            name='maestro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cgc_personal', to='app.personaleducativo'),
        ),
        migrations.AddField(
            model_name='ciclo_grado',
            name='grado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cg_grado', to='app.grado'),
        ),
        migrations.AddField(
            model_name='ciclo_grado',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cg_seccion', to='app.seccion'),
        ),
        migrations.CreateModel(
            name='Centropersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_centropersona', models.BooleanField(default=True)),
                ('centro_Educativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_educativo', to='app.centro_educativo')),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_educativo', to='app.personaleducativo')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_beneficiado', models.BooleanField(default=True)),
                ('estudios_anteriores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='B_estudios', to='app.estudiosant')),
                ('gen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='B_genero', to='app.genero')),
                ('ocup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='B_ocupacion', to='app.ocupacion')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='B_persona', to='app.persona')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='B_tutor', to='app.tutormuni')),
            ],
        ),
        migrations.CreateModel(
            name='AusenBeneficiado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('estado', models.BooleanField(default=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='A_areaM', to='app.area')),
                ('beneficiado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='B_beneficiadoM', to='app.beneficiado')),
            ],
        ),
        migrations.CreateModel(
            name='Apadecimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tratamiento', models.CharField(max_length=205)),
                ('lugar', models.CharField(max_length=205)),
                ('estado_Alpadecimiento', models.BooleanField(default=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='P_alumno', to='app.alumno')),
                ('padecimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='A_padecimiento', to='app.padecimiento')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='estudios_anteriores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EA_estudios', to='app.estudiosant'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='etni',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='E_etnia', to='app.etnia'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='gen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='G_genero', to='app.genero'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='idiome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='I_idioma', to='app.idioma'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='muni',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='M_muni', to='app.municipio'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='ocup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='O_ocupacion', to='app.ocupacion'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='T_tutor', to='app.tutor'),
        ),
    ]
