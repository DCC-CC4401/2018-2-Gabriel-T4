from django.db import models
from django.contrib.auth.models import User

ESTUDIANTE = 1
PROFESOR = 2
AUXILIAR = 3
AYUDANTE = 4


class Usuario(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    tipo = ((ESTUDIANTE, 'Estudiante'),
            (PROFESOR, 'Profesor'),
            (AUXILIAR, 'Auxiliar'),
            (AYUDANTE, 'Ayudante'),)
    rut = models.IntegerField()
    # TODO cambiar almacenamiento contraseña VERSION MUY PRELIMINAR, ESTO HAY QUE CAMBIARLO
    password = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    tipo_usuario = models.IntegerField(choices=tipo)

    def __str__(self):
        return '{}, {}'.format(self.apellido, self.nombre)

    def es_docente(self):
        return self.tipo_usuario != ESTUDIANTE

    def es_alumno(self):
        return self.tipo_usuario == ESTUDIANTE

    def cursos_activos_usuario(self):
        cursos_activos = Curso.objects.filter(activo=True)
        return [c for c in cursos_activos if cursos_activos.filter(rut=self.rut).count() > 0]


