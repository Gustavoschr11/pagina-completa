from django.shortcuts import render, redirect
from .forms import ContactoForm

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gracias')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})

def inicio(request):
    return render(request, 'inicio.html')

def escuela(request):
    return render(request, 'escuela.html')

def musica(request):
    return render(request, 'musica.html')

def gracias(request):
    return render(request, 'gracias.html')
