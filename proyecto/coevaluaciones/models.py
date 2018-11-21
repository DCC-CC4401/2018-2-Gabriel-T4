from django.db import models

# Create your models here.

class Usuario(models.Model):
    rut = models.IntegerField()
    # VERSION MUY PRELIMINAR, ESTO HAY QUE CAMBIARLO
    password = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    tipo_usuario = models.IntegerField()

    def __str__(self):
        return '{}, {}'.format(self.apellido, self.nombre)

class Ramo(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.codigo, self.nombre)


class Curso(models.Model):
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
                                        'Otoño' if self.semestre==0 else 'Primavera')


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
    #llaves que identifican el usuario y el curso en el que se realiza la modificacion
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    #accion que se realiza, deberiamos usar EnumTypes pa identificar entre
    # estudiante, prof, ... y para accion agregado, borrado
    accion = models.IntegerField()
    rol = models.IntegerField()

    # tiempo en el que ocurrio la modificacion
    fecha = models.DateTimeField()


class HistorialGrupos(models.Model):
    # identificacion del curso al que perteneces el grupo donde se hizo la modificacion
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)

    # identificacion del grupo en donde ocurrio el cambio
    grupo = models.ForeignKey(Grupo, on_delete=models.DO_NOTHING)

    # nuevo estado del grupo
    nombre_grupo = models.CharField(max_length=30)
    integrantes = models.ManyToManyField(Usuario)
    accion = models.IntegerField()


# aca empieza lo relacionado con las coevaluaciones, todavia no se hace el link entre coevaluacion y ramos




