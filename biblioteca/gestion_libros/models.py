from django.db import models
from faker import Faker

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento= models.DateField()
    
    def __str__(self):
        return self.nombre

class  Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)  
    
    def __str__(self):
        return self.nombre    
    
class Libro(models.Model):
    titulo=models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)  
    fecha_publicacion = models.DateField()
    precio = models.DecimalField(max_digits=16, decimal_places=2)
    editorial =models.ForeignKey(Editorial, on_delete=models.CASCADE, default=1)
    
    
    def __str__(self):
        return self.titulo
    

     
