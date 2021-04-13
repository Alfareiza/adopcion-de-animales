from django.db import models

# Create your models here.
# Informacion de persona que va a solicitar la adopcion de la mascota
# Field types: https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types

class Persona(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=75)
    telefono = models.CharField(max_length=12)
    edad = models.IntegerField()
    correo = models.EmailField()
    direccion = models.TextField(max_length=75)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
