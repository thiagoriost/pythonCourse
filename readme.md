# 1 Test version python
python --version

# 1.1 paquete de python para crear ambientes virtuales
pip install virtualenv

# 1.2 Crear ambiente virtual
python -m venv ~/.envs/[nombreFolderDondeGuardaraPaquetesDePython]
Ejemple_1: python -m venv our_venv


# 2 Activar entorno virtual => este no es necezario
oprimir f1 y selecionar python interprete
y seleccionar el recomendado

# 3 instalar django
pip install Django

# 4 ver admin de django
django-admin --help

# 5 crear poyecto
django-admin startproject [nombre_proyecto] .
ejem: django-admin startproject my_first_project .

# 6 revisar manage
python manage.py --help

# 7 iniciar servidor
python manage.py runserver

# 8 Crear aplicación dentro del proyecto
- detener server
python manage.py startapp my_first_app

# 9 Registrar la app
en settings.py buscar E:\software\PYTHON\my_first_project\my_first_project\settings.py
dentro de la carpeta del proyecto creado, ubicar l archivo settings.py y add la app creada

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_first_app',
]

# 9.1 migrar el proyecto, para crear tablas necesarias para el modelo
con el siguietne comando
python manage.py migrate
ejecutar el paso # 7, para validar la correcta ejecución

# 10 Django REST framework
pip install djangorestframework
- adionanrlo en app como esta en el paso # 9

# 11 instalación modulo para comuicar backend con frontend
https://pypi.org/project/django-cors-headers/
para autorizar a un servidor para q se conecte con el servidor de backend
pip install django-cors-headers
- adionanrlo en app como esta en el paso # 9
- adionanrlo en MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.common.CommonMiddleware'
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 12 autorizar quien se debe conectar al servidor
copiar lo siguiente de https://pypi.org/project/django-cors-headers/
al final del archivo settings.py 
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]
y ajustar a la necesidad

# creacion de tablas
con RM en la carpeta de la app, buscar el archivo models.py
- crear el screp q crea las clases que apunta a cada tabla
- comando q crea el script para las tablas: 
### python manage.py makemigrations [nombre de la app]
ej:
### python manage.py makemigrations my_task_app
- con lo anterior se creo el codigo q crea la tabla, ahora se debe ejecutar el 
comando que crea la tabla dentro de dbsqlite3:
### python manage.py migrate [nombre de la app]
ej:
#### python manage.py migrate my_task_app

# 13 crear usuario admin
para probar lo q se lelva hasta el momento
ejecutar los siguietnes comandos
python manage.py createsuperuser
ejecutar el paso 7
ingresar a
http://127.0.0.1:8000/admin/login/?next=/admin/
y emplear las credenciales creadas "admin_1234"

## Añadir al panel del administrador
en la carpeta de la app, en admin.py add los siguiente
admin.site.register([nombreDelModeloA_Añadir_queEstaEnElArchivoModels])
eje:
admin.site.register(Task)
En la juega con la importación del modelo

from django.contrib import admin
from .models import Task

#### Register your models here.
admin.site.register(Task)

actualizar la pagina del servidor

# crear el serializer.py para manejar datos en json
en la carpeta de la app crear el serializer.py

# 14 Crear las vistas
en el archivo views.py ubicado en la carpeta de apps
aqui se maneja los cruds con la ayuda de rest_framework

# 14 definir ruta q el front va a consultar
en la carpeta app en el urls.py si no existe crearlo


# 14.1 set routs en proyecto
abrir el file urls.py ubicado en la carpeta del proyecto
definir la vista asegurandose de q este importada, asi:

from my_first_app.views import my_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car-list/', my_view),
]

ejecutar el server como en el # 7

# Instar tool para documentar la api NO FUNCIONO
1. pip install setuptools
2. pip install coreapi
3. set settings.py
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'corsheaders',
            'rest_framework', 
            'coreapi',
            'my_task_app',
        ]
4. agregar paths en urlpatterns