# Generated by Django 3.2.7 on 2021-11-23 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apadecimiento',
            name='lugar',
            field=models.CharField(blank=True, max_length=205, null=True),
        ),
        migrations.AlterField(
            model_name='aspectoslab',
            name='familia_migrante',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='aspectossalud',
            name='fractura',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='aspectossalud',
            name='limitacion_fisica',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='aspectossalud',
            name='operacion',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='aspectossalud',
            name='padecimiento',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='aspectossalud',
            name='recibe_tratamiento',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comisionna',
            name='cg_comision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carg_comina', to='app.cargogrupo'),
        ),
        migrations.AlterField(
            model_name='comisionna',
            name='gorg_comision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gorga_comina', to='app.gorganizado'),
        ),
        migrations.AlterField(
            model_name='infoeducacion',
            name='conocimiento_leyes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lidercomunitario',
            name='escribir_l',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lidercomunitario',
            name='leer_l',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lidercomunitario',
            name='programa_c',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='P_ceipa', to='app.programac'),
        ),
        migrations.AlterField(
            model_name='lidercomunitario',
            name='vacuna_covid_l',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='padresfamilia',
            name='cantidad_hijos',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='cui_persona',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='personabasica',
            name='razon',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='psicologico',
            name='fecha_Analisis',
            field=models.DateField(),
        ),
    ]
