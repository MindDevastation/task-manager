from django.contrib import admin
from .models import Task, TaskType, Position

admin.site.register(Task)
admin.site.register(TaskType)
admin.site.register(Position)