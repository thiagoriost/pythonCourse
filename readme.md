# 1 Test version python
python --version

# 1.1 paquete de python para crear ambientes virtuales
pip install virtualenv

# 1.2 Crear ambiente virtual
python -m venv ~/.envs/[nombreFolderDondeGuardaraPaquetesDePython]
python -m venv nombre_entorno
python -m venv coffee_shop_env
Ejemple_1: cd pl    


# 2 Activar entorno virtual 
## - opcion 1:
    oprimir f1 y selecionar python interprete
    y seleccionar el recomendado
## - opcion 2:
    nombre_entorno\Scripts\activate

# 2.1 desactivar entorno virtual
deactivate

# 2.3 Validar paquetes instalados en el actual enviroment
    pip freeze

# 2.2 generar archivo requirements.txt
ejecutar lo siguiente para generar archivo:
    pip freeze > requirements.txt
para ejecutar el requirements.txt se ejcuta lo siguiente
    pip install -r requirements.txt
y si existe
    pip install -r requirements-dev.txt

# 3 instalar django
pip install Django

# 4 ver admin de django
django-admin --help

# 5 crear poyecto
django-admin startproject [nombre_proyecto]
django-admin startproject coffee_shop_project
ejem: django-admin startproject my_first_project .

# 6 revisar manage
python manage.py --help

# 7 iniciar servidor
python manage.py runserver

# 8 Crear aplicación dentro del proyecto
- detener server
python manage.py startapp products_app

# 8.1 Crear Modelos

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

# 12.1 creacion de tablas
    - con lo anterior se creo el codigo q crea la tabla, ahora se debe ejecutar el 
    comando que crea la tabla dentro de dbsqlite3:
    python manage.py migrate
    con RM en la carpeta de la app, buscar el archivo models.py
    - crear el screp q crea las clases que apunta a cada tabla
    - comando q crea el script para las tablas, esto basado en las clases dentro de los archivos en app/models: 
    python manage.py makemigrations
    revisar el archivo 0001_initial.py
    E:\software\PYTHON\platzy\Django\my_first_project\app_of_myfirstproyect\migrations\0001_initial.py

# 12.2 Comando para conectarse a la Db y ver las tablas
1 python manage.py dbshell
    (con .quit se sale de la DB)
2 ejectar 
    2.1 .tables => se ven las tablas en la DB Sqlite
    2.2 .schema [nombreTablaOseaModelo_extraido_del_paso_anterior]
    2.3 select * from [nombreTablaOseaModelo_extraido_del_paso_anterior];
3 Cada vez que se realizan cambios en algun modelo se debe ejecutar
    3.1 python manage.py makemigrations
    3.2 python manage.py migrate

# 12.3 Modificar datos de la DB

## NOTA: abrir dos terminales cmd o commans promp
    en una ejecutar el python manage.py dbshell => para ver tablas, schemas, select, etc
    y en la otra terminal ejecutar python manage.py shell para interactuar con la DB osea crud

    python manage.py shell => con lo anterior se ejecuta la terminal de python
    control + d => para salir de la shell

    from app_of_myfirstproyect.models import Car # importar modelo
    # con lo siguiente se crea un registro
    my_car?? # muestra info de la clase o modelo
    my_car = Car(title="BMW", year="2023", color="Blue") #instanciar modelo o clase enviandole los parametros o campos de la tabla
    my_car.save() # guardar registro

    my_car.title = "Mazda" # queda en memoria
    my_car.save() # guardar registro

    book = Book.objects.first()
    <!-- book = Book.objects.last() -->
    book ¬


    authors_list = [thiago, Audry]
    print(authors_list)
    book.authors.set(authors_list)

    Author.objects.create(name="Vale", bird_date="1985-08-15")
    Author.objects.all()
    Author.objects.filter(name="Thiago")
    Author.objects.filter(name="Audry").delete()
    Author.objects.all().order_by('name')

# 12.4 Relacion entre tablas


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


# shell
python manage.py shell
from django.http import HttpRequest
request = HttpRequest()
request.__dict__
