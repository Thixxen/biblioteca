from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'editorial', 'fecha_publicacion']

class BuscarLibroForm(forms.Form):
    titulo = forms.CharField(max_length=100)
