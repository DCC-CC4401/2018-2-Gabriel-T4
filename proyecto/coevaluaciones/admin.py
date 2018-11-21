from django.contrib import admin

# Register your models here.
from coevaluaciones.models import Usuario, Curso, Ramo, Grupo

admin.site.register(Usuario)
admin.site.register(Ramo)
admin.site.register(Curso)
admin.site.register(Grupo)
