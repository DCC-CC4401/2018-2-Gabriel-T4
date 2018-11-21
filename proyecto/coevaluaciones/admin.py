from django.contrib import admin

# Register your models here.
from coevaluaciones.models import Usuario, Curso, Ramo, Grupo, HistorialRoles, HistorialGrupos, Pregunta, Cuestionario

admin.site.register(Usuario)
admin.site.register(Ramo)
admin.site.register(Curso)
admin.site.register(Grupo)
admin.site.register(HistorialRoles)
admin.site.register(HistorialGrupos)

admin.site.register(Pregunta)
admin.site.register(Cuestionario)