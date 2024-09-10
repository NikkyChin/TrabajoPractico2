
# mensajes/views.py
from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm

def crear_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensajes_recibidos')
    else:
        form = MensajeForm()
    return render(request, 'mensajes/crear_mensaje.html', {'form': form})

