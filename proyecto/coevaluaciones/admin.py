from django.contrib import admin
from proyecto.coevaluaciones.models import Usuario, Curso, Ramo, Grupo, HistorialRoles, HistorialGrupos, Pregunta,\
    Cuestionario

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Ramo)
admin.site.register(Curso)
admin.site.register(Grupo)
admin.site.register(HistorialRoles)
admin.site.register(HistorialGrupos)

admin.site.register(Pregunta)
admin.site.register(Cuestionario)
