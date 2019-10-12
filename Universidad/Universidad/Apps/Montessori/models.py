from django.db import models


# Create your models here.


class Alumno(models.Model):
    Codigo = models.CharField(max_length=45)
    Nombre1 = models.CharField(max_length=45)
    Nombre2 = models.CharField(max_length=45)
    ApellidoP = models.CharField(max_length=45)
    ApellidoM = models.CharField(max_length=45)
    FechaNacimiento = models.DateField()
    GENERO = (('F', 'Femenino'), ('M', 'Masculino'))
    genero = models.CharField(max_length=1, choices=GENERO, default='M')


    def NombreCompleto(self):
        cadena = "{0} {1}, {2} {3}"
        return cadena.format(self.Nombre1, self.Nombre2, self.ApellidoP, self.ApellidoM)
 
    def __str__(self):
        return self.NombreCompleto()


class Curso(models.Model):
    Nombre = models.CharField(max_length=45)
    Creditos = models.PositiveIntegerField()
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.Nombre, self.Creditos)

class Matricula(models.Model):
    estado = models.CharField(max_length=45, default='DEFAULT VALUE')
    Alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE, default='DEFAULT VALUE')
    Curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE, default='DEFAULT VALUE')
    FechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Alumno, self.Curso.Nombre)

class Carrera(models.Model):
    Codigo = models.CharField(max_length=45, default='DEFAULT VALUE')
    Nombre = models.CharField(max_length=45)
    id_alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE, default='DEFAULT VALUE')

  def __str__(self):
    cadena = "{0} => {1}"
    return cadena.format(self.Nombre, self.id_alumno.Nombre)

      
      
        