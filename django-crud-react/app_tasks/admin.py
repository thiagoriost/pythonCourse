from django.contrib import admin
from .models import TaskClass, Task_2_Class

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    model = TaskClass
    list_display = ['title', 'description', 'done']
    search_fields = ['title', 'description', 'done']

class TaskAdmin_2(admin.ModelAdmin):
    model = Task_2_Class
    list_display = ['title_2', 'description_2', 'done_2', 'prueba']
    search_fields = ['title_2', 'description_2', 'done_2', 'prueba']

admin.site.register(TaskClass, TaskAdmin)
admin.site.register(Task_2_Class, TaskAdmin_2)
