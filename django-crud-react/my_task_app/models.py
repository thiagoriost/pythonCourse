from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    
    # con lo siguientes se configura para que sea el titulo el q se muestre en
    # el administrador de tareas
    def __str__(self):
        return self.title
    
    # set campos a serializar para manejoarlos como json
    