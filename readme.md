# 1 Crear ambiente virtual
python -m venv ~/.envs/[nombreFolderEnveroment]
Ejemple_1: python -m venv ~/.envs/my-first-enviroment
Ejemple_2: python -m venv ~/.envs/my-secont-enviroment

# 2 Activar entorno virtual => este no es necezario
source ~/.envs/[nombreFolderEnveroment]/bin/activate

# 3 instalar django
pip install Django

# 4 ver admin de django
django-admin --help

# 5 inicializar poyecto
django-admin startproject [nombre_proyecto]
ejem: django-admin startproject my_first_project

# 6 revisar manage
python manage.py --help

# 7 iniciar servidor
python manage.py runserver

# 8 Crear aplicación dentro del proyecto
python manage.py startapp my_first_app

# 9 Registrar la app
en settings.py buscar E:\software\PYTHON\my_first_project\my_first_project\settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_first_app',
]

# 10 create folder templates
en my_first_app, crear carpeta templates/[nobreDeLaApp]/[nombre archivo html de la vista]
ejemplo: my_first_project\my_first_app\templates\my_fisrt_app\car_list.html

# 11 definir ruta del template html
en
\my_first_project\my_first_project\urls.py

definir la vista asegurandose de q este importada, asi:

from my_first_app.views import my_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car-list/', my_view),
]

ejecutar el server como en el # 7

