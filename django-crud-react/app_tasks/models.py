from django.db import models

# Create your models here.
class TaskClass(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)

    def __str__(self): #con este metodo se muestra el titulo en el admin
        return self.title
    
class Task_2_Class(models.Model):
    title_2 = models.CharField(max_length=200)
    description_2 = models.TextField(blank=True)
    done_2 = models.BooleanField(default=False)
    prueba = models.TextField(blank=True, max_length=20)

    def __str__(self): #con este metodo se muestra el titulo en el admin
        return self.title_2