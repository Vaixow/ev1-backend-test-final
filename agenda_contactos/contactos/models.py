from django.db import models

class Contacto(models.Model): ##modelo de contacto
    nombre = models.CharField(max_length=100) ##le asignamos el tamaño y el tipo de string
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.correo}"
# Create your models here.
