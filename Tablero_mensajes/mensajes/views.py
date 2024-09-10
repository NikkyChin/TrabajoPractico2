# mensajes/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mensaje
from .forms import MensajeForm, FiltroMensajeForm

def crear_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensajes:ver_recibidos')
    else:
        form = MensajeForm()
    return render(request, 'crear_mensaje.html', {'form': form})

def ver_mensajes_recibidos(request):
    form = FiltroMensajeForm(request.GET)
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        if nombre:
            mensajes = Mensaje.objects.filter(destinatario=nombre)
        else:
            mensajes = Mensaje.objects.filter(destinatario=request.user.username)
    else:
        mensajes = Mensaje.objects.filter(destinatario=request.user.username)
    
    return render(request, 'ver_mensajes_recibidos.html', {'mensajes': mensajes, 'form': form})

def ver_mensajes_enviados(request):
    form = FiltroMensajeForm(request.GET)
    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        if nombre:
            mensajes = Mensaje.objects.filter(remitente=nombre)
        else:
            mensajes = Mensaje.objects.filter(remitente=request.user.username)
    else:
        mensajes = Mensaje.objects.filter(remitente=request.user.username)
    
    return render(request, 'ver_mensajes_enviados.html', {'mensajes': mensajes, 'form': form})

def eliminar_mensaje(request, id):
    mensaje = get_object_or_404(Mensaje, id=id)
    mensaje.delete()
    return redirect('mensajes:ver_recibidos')

def index(request):
    return render(request, 'base.html')
