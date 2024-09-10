# mensajes/urls.py
from django.urls import path
from . import views

app_name = 'mensajes'  # Esto es útil para nombres de ruta con namespace

urlpatterns = [
    path('crear/', views.crear_mensaje, name='crear_mensaje'),  # Vista para crear mensajes
    path('recibidos/', views.ver_mensajes_recibidos, name='ver_recibidos'),  # Vista para ver mensajes recibidos
    path('enviados/', views.ver_mensajes_enviados, name='ver_enviados'),  # Vista para ver mensajes enviados
    path('eliminar/<int:id>/', views.eliminar_mensaje, name='eliminar_mensaje'),  # Vista para eliminar mensajes
    
]
