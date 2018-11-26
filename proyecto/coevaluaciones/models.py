from django.db import models

# Create your models here.


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return '{}, {}'.format(self.apellido, self.nombre)


class Ramo(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.codigo, self.nombre)


class Curso(models.Model):
    ramo = models.ForeignKey(Ramo, on_delete=models.SET_NULL, null=True)
    anno = models.IntegerField()
    semestre = models.IntegerField()
    seccion = models.IntegerField()
    listaDeAlumnos = models.OneToOneField('listaAlumnos', related_name='lista_alumnos', blank=True, null=True,
                                          on_delete=models.DO_NOTHING)
    listaDeProfesores= models.OneToOneField('listaProfesores', related_name='lista_profesores', blank=True,
                                            null=True, on_delete=models.DO_NOTHING)
    listaDeAuxiliares = models.OneToOneField('listaAuxiliares', related_name='lista_auxiliares', blank=True,
                                             null=True, on_delete=models.DO_NOTHING)
    listaDeAyudantes = models.OneToOneField('listaAyudantes', related_name='lista_ayudantes', blank=True,
                                            null=True, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('ramo', 'anno', 'semestre', 'seccion')

    def __str__(self):
        return '{}-{} {} {}, {}'.format(self.ramo.codigo,
                                     self.seccion,
                                     self.ramo.nombre,
                                     self.anno,
                                     'Otoño' if self.semestre == 0 else 'Primavera')


class Grupo (models.Model):
    integrantes = models.ForeignKey(Usuario, null=True, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=30)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    activo = models.BooleanField()

    def __str__(self):
        return str(self.nombre)


class ListaAlumnos(models.Model):
    curso = models.OneToOneField(Curso, on_delete=models.DO_NOTHING)
    alumnos = models.ManyToManyField(Usuario)

    def __str__(self):
        return 'Lista de Alumnos de: ' + str(self.curso.ramo.codigo)


class ListaProfesores(models.Model):
    curso = models.OneToOneField(Curso, on_delete=models.DO_NOTHING)
    profesores = models.ManyToManyField(Usuario)

    def __str__(self):
        return 'Lista de Profesores de: ' + str(self.curso.ramo.codigo)


class ListaAuxiliares(models.Model):
    curso = models.OneToOneField(Curso, on_delete=models.DO_NOTHING)
    auxiliares = models.ManyToManyField(Usuario)

    def __str__(self):
        return 'Lista de Axuliares de: ' + str(self.curso.ramo.codigo)


class ListaAyudantes(models.Model):
    curso = models.OneToOneField(Curso, on_delete=models.DO_NOTHING)
    ayudantes = models.ManyToManyField(Usuario)

    def __str__(self):
        return 'Lista de Ayudantes de: ' + str(self.curso.ramo.codigo)


class Pregunta(models.Model):
    interrogante = models.TextField(default='Escriba la interrogante a preguntar')
    nota = 'nota'
    texto = 'texto'
    tipos = ((nota, 'nota'),
             (texto, 'texto'),)
    tipo = models.CharField(max_length=10, choices=tipos)

    def __str__(self):
        return 'Pregunta ' + str(self.id)


class Cuestionario(models.Model):
    nombre = models.CharField(max_length=30)
    listaDePreguntas= models.ManyToManyField(Pregunta, blank=True)

    def __str__(self):
        return self.nombre


class Coevaluaciones(models.Model):
    id_Coeavaluacion = models.IntegerField(primary_key=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.BooleanField()
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Coevaluación ' + self.curso.ramo.nombre + ': ' + self.cuestionario.nombre


class HistorialAlumnos(models.Model):
    usuario = models.OneToOneField(Usuario, null=True, on_delete=models.DO_NOTHING)
    cursos = models.ForeignKey(Curso, null=True, on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Ultima modificación: ' + str(self.fecha)


class HistorialCursos(models.Model):
    rut = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    grupo = models.ForeignKey(Grupo, on_delete=models.DO_NOTHING)
    borrado = 0
    agregado = 1
    creado = 2
    acciones = ((borrado, 0),
                (agregado, 1),
                (creado, 2),)
    accion = models.IntegerField(choices=acciones)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Última modificación: ' + str(self.fecha)


class Resultados(models.Model):
    idCoev = models.ForeignKey(Coevaluaciones, on_delete=models.DO_NOTHING)
    rut_evaluador = models.ForeignKey(Usuario, related_name='evaluador', on_delete=models.DO_NOTHING)
    rut_evaluado = models.ForeignKey(Usuario, related_name='evaluado', on_delete=models.DO_NOTHING)
    preguntas = models.ForeignKey(Cuestionario, on_delete=models.DO_NOTHING)
    respuesta = models.TextField()

    def __str__(self):
        return 'Resultados de ' + str(self.rut_evaluado)
