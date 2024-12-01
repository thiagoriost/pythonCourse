from django.urls import path, include
from rest_framework import routers
from my_task_app import  views

# api versioning
router = routers.DefaultRouter()
router.register(r'my_task_app', views.TaskView, 'tasks')

urlpatterns = [
    path('api/v1', include(router.urls))
]
# con lo anterior se configura las rutas para el GET POST PUT DELETE
# para problarlo se necesita un cliente rest
