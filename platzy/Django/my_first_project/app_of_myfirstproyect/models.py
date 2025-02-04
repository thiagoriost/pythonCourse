from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=250, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.year} - {self.color}"
    
class Publisher(models.Model):
    name = models.TextField(max_length=200)
    addres = models.TextField(max_length=200)
    
    def __str__(self):
        return f"{self.name} - {self.addres}"

class Author(models.Model):
    name = models.TextField(max_length=200)
    bird_date = models.DateField()
    
    def __str__(self):
        return f"{self.name} - {self.bird_date}"
        
class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    webSite = models.URLField()
    biography = models.TextField(max_length=500)
    
    def __str__(self):
        return f"{self.webSite} - {self.biography}"

class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE) #con CASCADE si se elimina el publisher se eliminan los libros
    authors = models.ManyToManyField(Author, related_name='authors')
    
    def __str__(self):
        return f"{self.title} - {self.publication_date} - {self.publisher} - {self.authors}"
    
