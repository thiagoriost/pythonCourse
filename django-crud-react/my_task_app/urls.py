from django.urls import path, include
from rest_framework import routers
from my_task_app import  views

# api versioning
router = routers.DefaultRouter()
router.register(r'my_task_app', views.TaskView, 'tasks')
# from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('api/v1/', include(router.urls)),
    #http://localhost:8000/tasks/car-list/my_task_app/
    # path('car-list/', include(router.urls))
    # path('docs/', include_docs_urls(title="Task API"))
]
# con lo anterior se configura las rutas para el GET POST PUT DELETE
# para problarlo se necesita un cliente rest
