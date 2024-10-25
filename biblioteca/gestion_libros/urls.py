from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.lista_libros,name='lista_libros'),
    path('libros/autor/<str:autor_nombre>', views.libros_por_autor,name='libros_por_autor'),
    path('libros/precio', views.libros_precio_alto,name='libros_precio'),
    path('libros/total_por_autor',views.total_precio_por_autor, name='total_precio_por_autor'),
    ]