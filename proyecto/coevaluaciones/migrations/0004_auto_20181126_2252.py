# Generated by Django 2.1.3 on 2018-11-26 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coevaluaciones', '0003_historialgrupos_historialroles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuestionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
                ('texto', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='historialgrupos',
            options={'verbose_name_plural': 'HistorialGrupos'},
        ),
        migrations.AlterModelOptions(
            name='historialroles',
            options={'verbose_name_plural': 'HistorialRoles'},
        ),
        migrations.AlterField(
            model_name='curso',
            name='alumnos',
            field=models.ManyToManyField(related_name='lista_alumnos', to='Usuarios.Usuario'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='auxiliares',
            field=models.ManyToManyField(related_name='lista_auxiliares', to='Usuarios.Usuario'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='ayudantes',
            field=models.ManyToManyField(related_name='lista_ayudantes', to='Usuarios.Usuario'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='profesores',
            field=models.ManyToManyField(related_name='lista_profesores', to='Usuarios.Usuario'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='integrantes',
            field=models.ManyToManyField(to='Usuarios.Usuario'),
        ),
        migrations.AlterField(
            model_name='historialgrupos',
            name='accion',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2)]),
        ),
        migrations.AlterField(
            model_name='historialgrupos',
            name='integrantes',
            field=models.ManyToManyField(to='Usuarios.Usuario'),
        ),
        migrations.AlterField(
            model_name='historialroles',
            name='accion',
            field=models.IntegerField(choices=[(0, 0), (1, 1)]),
        ),
        migrations.AlterField(
            model_name='historialroles',
            name='rol',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
        migrations.AlterField(
            model_name='historialroles',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Usuarios.Usuario'),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='preguntas',
            field=models.ManyToManyField(to='coevaluaciones.Pregunta'),
        ),
    ]
