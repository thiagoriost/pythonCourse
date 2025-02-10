from rest_framework import viewsets
from .models import TaskClass, Task_2_Class
from .serializer import TaskSerializer, TaskSerializer_2

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskClass.objects.all()
    serializer_class = TaskSerializer

class TaskView_2_Set(viewsets.ModelViewSet):
    queryset = Task_2_Class.objects.all()
    serializer_class = TaskSerializer_2
