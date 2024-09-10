# Tablero de Mensajes

Este es un proyecto Django que permite gestionar mensajes entre usuarios. Incluye funcionalidades para crear, ver y eliminar mensajes.

## Instalación y Configuración en Windows

### Requisitos Previos

- [Python](https://www.python.org/downloads/) 3.12 o superior.
- [Pip](https://pip.pypa.io/en/stable/) (gestor de paquetes para Python).
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (opcional, para clonar el repositorio).

### Pasos para la Instalación

1. **Clonar el Repositorio**

   Abre una terminal (cmd o PowerShell) y ejecuta el siguiente comando para clonar el repositorio:

   git clone https://github.com/NikkyChin/TrabajoPractico2.git


2. **Navegar al Directorio del Proyecto**

   Cambia al directorio del proyecto:

   cd TrabajoPractico2


3. **Crear un Entorno Virtual**

   Es una buena práctica usar un entorno virtual para gestionar las dependencias. Ejecuta:

   python -m venv env


4. **Activar el Entorno Virtual**

   Activa el entorno virtual:

   .\env\Scripts\activate
  

5. **Instalar las Dependencias**

   Con el entorno virtual activado, instala las dependencias del proyecto usando `pip`:

   pip install -r requirements.txt


6. **Configurar la Base de Datos**

   Ejecuta las migraciones para configurar la base de datos:

   python manage.py migrate


7. **Crear un Superusuario (opcional)**

   Si deseas acceder al panel de administración, crea un superusuario:

   python manage.py createsuperuser


8. **Iniciar el Servidor de Desarrollo**

   Finalmente, inicia el servidor de desarrollo:

   python manage.py runserver
   

   Puedes acceder a la aplicación en tu navegador web en `http://127.0.0.1:8000/`.

## Uso

- **Crear Mensaje**: Navega a `http://127.0.0.1:8000/mensajes/crear/` para crear un nuevo mensaje.
- **Ver Mensajes Recibidos**: Accede a `http://127.0.0.1:8000/mensajes/recibidos/` para ver los mensajes recibidos.
- **Ver Mensajes Enviados**: Visita `http://127.0.0.1:8000/mensajes/enviados/` para ver los mensajes enviados.
