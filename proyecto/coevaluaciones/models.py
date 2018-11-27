from django.db import models
from django.contrib.auth.models import User
from Usuarios.models import Usuario
from Cursos.models import Curso, Grupo

# aca empieza lo relacionado con las coevaluaciones, todavia no se hace el link entre coevaluacion y ramos

PREGUNTA_1a7 = 1
PREGUNTA_TXT = 2
PREGUNTA_NUM = 3


class Pregunta(models.Model):
    tipo = models.IntegerField(choices=((PREGUNTA_1a7, 'Escala de 1 a 7'),
                                        (PREGUNTA_NUM, 'Valor numérico'),
                                        (PREGUNTA_TXT, 'Texto plano')))
    texto = models.TextField()

    def __str__(self):
        return 'Pregunta ' + self.id


class Cuestionario(models.Model):
    nombre = models.CharField(max_length=30)
    preguntas = models.ManyToManyField(Pregunta)

    def __str__(self):
        return self.nombre


class Coevaluacion(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.DO_NOTHING)
    fecha_creada = models.DateField()
    fecha_abierta = models.DateField()
    fecha_cierre = models.DateField()


class RespuestaCoevaluacion(models.Model):
    respondiente = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    coevaluacion = models.ForeignKey(Coevaluacion)


class RespuestaCoevaluacionEvaluado(models.Model):
    respuesta_coev = models.ForeignKey(RespuestaCoevaluacion, on_delete=models.DO_NOTHING)
    evaluado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)


class RespuestaCoevaluacionEvaluadoPregunta(models.Model):
    respuesta_coev_evaluado = models.ForeignKey(RespuestaCoevaluacionEvaluado, on_delete=models.DO_NOTHING)
    respuesta_numerica = models.IntegerField()
    respuesta_texto = models.TextField()
    respuesta_escala = models.IntegerField(choices=list(zip(*(lambda x: (x, list(map(str, x))))(list(range(1,8))))))
