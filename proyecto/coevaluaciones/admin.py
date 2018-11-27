from django.contrib import admin
from coevaluaciones.models import Usuario, Curso, Ramo, Grupo, Pregunta, Cuestionario, ListaAlumnos,\
    ListaProfesores, ListaAuxiliares, ListaAyudantes, Coevaluaciones, HistorialAlumnos, HistorialCursos

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Ramo)
admin.site.register(Curso)
admin.site.register(Grupo)
admin.site.register(Pregunta)
admin.site.register(Cuestionario)
admin.site.register(ListaAlumnos)
admin.site.register(ListaAuxiliares)
admin.site.register(ListaAyudantes)
admin.site.register(ListaProfesores)
admin.site.register(Coevaluaciones)
admin.site.register(HistorialAlumnos)
admin.site.register(HistorialCursos)