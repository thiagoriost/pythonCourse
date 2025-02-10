from rest_framework import serializers
from .models import TaskClass, Task_2_Class


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskClass
        fields = '__all__'

class TaskSerializer_2(serializers.ModelSerializer):
    class Meta:
        model = Task_2_Class
        fields = '__all__'