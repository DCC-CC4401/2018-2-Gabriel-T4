from django.db import models

# Create your models here.


class Usuario(models.Model):
    estudiante = 1
    profesor = 2
    auxiliar = 3
    ayudante = 4
    tipo = ((estudiante, 1),
            (profesor, 2),
            (auxiliar, 3),
            (ayudante, 4),)
    rut = models.IntegerField()
    # TODO cambiar almacenamiento contraseña VERSION MUY PRELIMINAR, ESTO HAY QUE CAMBIARLO
    password = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    tipo_usuario = models.IntegerField(choices=tipo)

    def __str__(self):
        return '{}, {}'.format(self.apellido, self.nombre)


class Ramo(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.codigo, self.nombre)


class Curso(models.Model):
    # TODO revisar on_delete
    codigo_ramo = models.ForeignKey(Ramo, on_delete=models.DO_NOTHING)
    anno = models.IntegerField()
    semestre = models.IntegerField()
    seccion = models.IntegerField()
    alumnos = models.ManyToManyField(Usuario, related_name='lista_alumnos')
    profesores = models.ManyToManyField(Usuario, related_name='lista_profesores')
    auxiliares = models.ManyToManyField(Usuario, related_name='lista_auxiliares')
    ayudantes = models.ManyToManyField(Usuario, related_name='lista_ayudantes')

    def __str__(self):
        return '{}-{} {} {}, {}'.format(self.codigo_ramo,
                                        self.seccion,
                                        Ramo.objects.get(codigo=self.codigo_ramo),
                                        self.anno,
                                        'Otoño' if self.semestre == 0 else 'Primavera')


class Grupo(models.Model):
    # identificacion del curso al que perteneces
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    # identificacion del grupo
    nombre = models.CharField(max_length=30)
    integrantes = models.ManyToManyField(Usuario)

    activo = models.BooleanField()

    def __str__(self):
        return self.nombre


class HistorialRoles(models.Model):
    estudiante = 1
    profesor = 2
    auxiliar = 3
    ayudante = 4
    tipo = ((estudiante, 1),
            (profesor, 2),
            (auxiliar, 3),
            (ayudante, 4),)
    borrar = 0
    agregar = 1
    acciones = ((borrar, 0),
                (agregar, 1),)

    # llaves que identifican el usuario y el curso en el que se realiza la modificacion
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    # TODO usar choices en los models
    # accion que se realiza, deberiamos usar EnumTypes pa identificar entre
    # estudiante, prof, ... y para accion agregado, borrado

    accion = models.IntegerField(choices=acciones)
    rol = models.IntegerField(choices=tipo)

    # tiempo en el que ocurrio la modificacion
    fecha = models.DateTimeField()

    def __str__(self):
        return self.fecha

    class Meta:
        verbose_name_plural = "HistorialRoles"


class HistorialGrupos(models.Model):
    borrar = 0
    agregar = 1
    crear = 2
    acciones = ((borrar, 0),
                (agregar, 1),
                (crear, 2),)

    # identificacion del curso al que perteneces el grupo donde se hizo la modificacion
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    # identificacion del grupo en donde ocurrio el cambio
    grupo = models.ForeignKey(Grupo, on_delete=models.DO_NOTHING)

    # nuevo estado del grupo
    nombre_grupo = models.CharField(max_length=30)
    integrantes = models.ManyToManyField(Usuario)
    # TODO usar choices
    accion = models.IntegerField(choices=acciones)

    def __str__(self):
        return self.fecha

    class Meta:
        verbose_name_plural = "HistorialGrupos"


# aca empieza lo relacionado con las coevaluaciones, todavia no se hace el link entre coevaluacion y ramos
class Pregunta(models.Model):
    tipo = models.CharField(max_length=10)
    texto = models.TextField()

    def __str__(self):
        return 'Pregunta ' + self.id


class Cuestionario(models.Model):
    nombre = models.CharField(max_length=30)
    preguntas = models.ManyToManyField(Pregunta)

    def __str__(self):
        return self.nombre


COEVALUACION_ABIERTA = True
COEVALUACION_CERRADA = False


class Coevaluacion(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.BooleanField()
    cuestionario = models.ForeignKey(Cuestionario)
    curso = models.ForeignKey(Curso)
