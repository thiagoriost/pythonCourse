from django.urls import path, include
from rest_framework import routers
from app_tasks.views import TaskViewSet, TaskView_2_Set

router = routers.DefaultRouter()
router.register(r'tareas', TaskViewSet)
router.register(r'tareas_2', TaskView_2_Set)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    # path('api/v1/', include(router.urls)),
]

