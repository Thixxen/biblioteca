from django.shortcuts import render, redirect
from .forms import InsertarLibroForm
from .models import Libro
from .forms import BuscarLibroForm

def insertar_libro(request):
    if request.method == 'POST':
        form = InsertarLibroForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo libro en la base de datos
            return redirect('libros/insertar_libro.html')  # Redirecciona a otra página después de guardar
    else:
        form = InsertarLibroForm()
    return render(request, 'libros/insertar_libro.html', {'form': form})



# Vista para buscar libros por título
def buscar_libro(request):
    if request.method == 'POST':
        form = BuscarLibroForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            libros = Libro.objects.filter(titulo__icontains=titulo)
            return render(request, 'libros/buscar_libro.html', {'libros': libros})
    else:
        form = BuscarLibroForm()
    return render(request, 'libros/buscar_libro.html', {'form': form})
