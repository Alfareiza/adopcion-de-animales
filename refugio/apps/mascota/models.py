from django.db import models

# Create your models here.
from refugio.apps.adopcion.models import Persona


class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"


class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_de_rescate = models.DateField()
    raza = models.CharField(max_length=10)
    comentarios = models.CharField(max_length=10)
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, blank=True)

    def __str__(self):
        return f"{self.nombre}"
