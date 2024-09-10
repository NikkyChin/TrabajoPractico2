from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm

# Crear mensajes
def crear_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensajes_recibidos')
    else:
        form = MensajeForm()
    return render(request, 'mensajes/crear_mensaje.html', {'form': form})

# Mensajes enviados
def mensajes_enviados(request):
    # Filtrar por un remitente específico
    mensajes = Mensaje.objects.filter(remitente='Juan')  # Ajustar según el remitente deseado
    return render(request, 'mensajes/mensajes_enviados.html', {'mensajes': mensajes})

# Mensajes recibidos
def mensajes_recibidos(request):
    # Filtrar por un destinatario específico
    mensajes = Mensaje.objects.filter(destinatario='Pedro')  # Ajustar según el destinatario deseado
    return render(request, 'mensajes/mensajes_recibidos.html', {'mensajes': mensajes})


# eliminar mensajes
def eliminar_mensaje(request, mensaje_id):
    mensaje = Mensaje.objects.get(id=mensaje_id)
    mensaje.delete()
    return redirect('mensajes_recibidos')
