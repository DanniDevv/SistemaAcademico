from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telefono = models.CharField(max_length=9)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Alumno(Persona):
    pass

class Docente(Persona):
    pass

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    id_docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    dia_semana = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return str(self.hora_inicio)

class Nota(models.Model):
    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    valor_nota = models.CharField(max_length=200)

    def __str__(self):
        return self.valor_nota

class Asistencia(models.Model):
    ASISTENCIA_CHOICES = (
        ('AS', 'Asistió'),
        ('NA', 'No asistió'),
    )

    id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    id_horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    fecha_asistencia = models.DateField()
    asistencia = models.CharField(max_length=2, null=True,choices=ASISTENCIA_CHOICES)


    def __str__(self):
        return f"{self.id_alumno} {self.asistencia}"