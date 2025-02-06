from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.TextField(max_length=200, verbose_name='Nombre')
    description = models.TextField(max_length=300, verbose_name='Descripción')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    available = models.BooleanField(default=True, verbose_name='Disponible')
    # photo = models.ImageField(upload_to='products/%Y/%m/%d', null=True, blank=True, verbose_name='Foto')
    photo = models.ImageField(upload_to='logos', null=True, blank=True, verbose_name='Foto')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación', null=True)
    
    def __str__(self):
        return self.name