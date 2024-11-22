from django.db import models

# Create your models here.
class Carro(models.Model):
    titulo = models.TextField(max_length=250)