# Generated by Django 3.2.7 on 2021-10-03 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PadresFamilia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leer', models.BooleanField(default=False)),
                ('escribir', models.BooleanField(default=False)),
                ('vacunaCovid', models.BooleanField(default=False)),
                ('participacionG', models.BooleanField(default=False)),
                ('estado_padres', models.BooleanField(default=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargoG_padre', to='app.cargogrupo')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupoOr_padre', to='app.gorganizado')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='per_padre', to='app.persona')),
                ('programaC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programa_padre', to='app.programac')),
            ],
        ),
        migrations.CreateModel(
            name='CorporacionMunicipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participacion', models.BooleanField(default=False)),
                ('vacuna', models.BooleanField(default=False)),
                ('estado_corporacion', models.BooleanField(default=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargoG_cm', to='app.cargogrupo')),
                ('comision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='com_cm', to='app.comision')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupoO_cm', to='app.gorganizado')),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidop_cm', to='app.partidopolitic')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pers_comision', to='app.persona')),
            ],
        ),
        migrations.CreateModel(
            name='ComisionNA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participacion', models.BooleanField(default=False)),
                ('estado_comision', models.BooleanField(default=True)),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insti_comision', to='app.institucion')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comision_pers', to='app.persona')),
            ],
        ),
        migrations.CreateModel(
            name='BeneficiadoArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(blank=True, max_length=250, null=True)),
                ('fecha', models.DateField()),
                ('estado_ba', models.BooleanField(default=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ba_Area', to='app.area')),
                ('beneficiado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ba_benef', to='app.beneficiado')),
                ('programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ba_programaC', to='app.programac')),
            ],
        ),
    ]