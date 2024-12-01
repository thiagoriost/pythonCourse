from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task


# Create your views here.

# con esta clase se setea el crud relacionado con el modelo y vista para task
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()