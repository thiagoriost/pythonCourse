# Crear ambiente virtual
python -m venv ~/.envs/[nombreFolderEnveroment]
Ejemple_1: python -m venv ~/.envs/my-first-enviroment
Ejemple_2: python -m venv ~/.envs/my-secont-enviroment

# Activar entorno virtual => este no es mecezario
source ~/.envs/[nombreFolderEnveroment]/bin/activate

# instalar django
pip install Django

# ver admin de django
django-admin --help

# inicializar poyecto
django-admin startproject [nombre_proyecto]
ejem: django-admin startproject my_first_project

# revisar manage
python manage.py --help

# iniciar servidor
python manage.py runserver

# Crear aplicación dentro del proyecto
python manage.py startapp my_first_app