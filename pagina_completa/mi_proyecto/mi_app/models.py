from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    pregunta1 = models.CharField(max_length=200)
    pregunta2 = models.CharField(max_length=200)
    pregunta3 = models.CharField(max_length=200)
    pregunta4 = models.CharField(max_length=200)
    pregunta5 = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


# Create your models here.
