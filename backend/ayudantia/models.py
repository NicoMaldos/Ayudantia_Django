from django.db import models

# Create your models here.
class Estudiantes(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    mail = models.EmailField(max_length=75)

    def _str_(self):
        return self.title

class Profesores(models.Model):
    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    mail = models.EmailField(max_length=75)