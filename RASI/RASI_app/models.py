from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.IntegerField()
    edad = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    grupo_sanguineo = models.CharField(max_length=50)   
    nombre_eps = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    dependecia = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre



class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.IntegerField()
    edad = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    grupo_sanguineo = models.CharField(max_length=50)   
    nombre_eps = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    imagen_diagnostico = models.ImageField(upload_to='images', null=True)

    def __str__(self):
        return self.nombre