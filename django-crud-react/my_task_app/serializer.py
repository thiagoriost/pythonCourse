from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # field = ('id', 'title', 'description', 'done')
        fields = '__all__' #agrega de forma automatica todos los campos del modelo
        