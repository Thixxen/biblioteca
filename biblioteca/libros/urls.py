from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from libros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', include('libros.urls')),
    path('LibroForm/', views.LibroForm, name='LibroForm'),  # Cambiado a 'insertar/' para evitar conflictos con la vista predeterminada
    path('buscar/', views.buscar_libro, name='buscar_libro'),
]



app_name = 'libros'