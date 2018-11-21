# Generated by Django 2.1.3 on 2018-11-21 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coevaluaciones', '0002_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistorialGrupos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_grupo', models.CharField(max_length=30)),
                ('accion', models.IntegerField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='coevaluaciones.Curso')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='coevaluaciones.Grupo')),
                ('integrantes', models.ManyToManyField(to='coevaluaciones.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion', models.IntegerField()),
                ('rol', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='coevaluaciones.Curso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='coevaluaciones.Usuario')),
            ],
        ),
    ]