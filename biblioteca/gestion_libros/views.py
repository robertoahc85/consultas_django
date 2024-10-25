from django.shortcuts import render
from .models import Libro
from django.db.models import Sum

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'gestion_libros/lista_libros.html',{'libros' : libros})

#conulta de libros filtrado por autor
def libros_por_autor(request,autor_nombre):
    libros = Libro.objects.filter(autor__nombre =autor_nombre)
    return render(request, 'gestion_libros/libros_por_autor.html',{'libros' :libros, 'autor': autor_nombre})
    
def libros_precio_alto(request):
    libros = Libro.objects.filter(precio__gte =30)
    return render(request, 'gestion_libros/libros_por_precio.html',{'libros' : libros})

def total_precio_por_autor(request):
    #agrupar libros por autor y sumar los precios
    total_por_autor = Libro.objects.values('autor__nombre').annotate(total_precio =Sum('precio'))
    return render(request,'gestion_libros/total_precio_autor.html',{'total_por_autor' : total_por_autor})

#Realizar un reporte qeu cuente los libros por autor, y que saque el promedio precio por autor.
    
# Create your views here.

#libros publicado despues del 2000