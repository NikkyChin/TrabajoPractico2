# mensajes/views.py
from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm

# crear mensajes
def crear_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensajes_recibidos')
    else:
        form = MensajeForm()
    return render(request, 'mensajes/crear_mensaje.html', {'form': form})

# mensajes enviados
def mensajes_enviados(request):
    mensajes = Mensaje.objects.filter(remitente='Juan')  # Ajustar para filtrar por el usuario logueado
    return render(request, 'mensajes/mensajes_enviados.html', {'mensajes': mensajes})

# mensajes recibidos
def mensajes_recibidos(request):
    mensajes = Mensaje.objects.filter(destinatario='pedro')  # Aquí se puede ajustar para que filtre por el usuario logueado
    return render(request, 'mensajes/mensajes_recibidos.html', {'mensajes': mensajes})

# eliminar mensajes
def eliminar_mensaje(request, mensaje_id):
    mensaje = Mensaje.objects.get(id=mensaje_id)
    mensaje.delete()
    return redirect('mensajes_recibidos')
