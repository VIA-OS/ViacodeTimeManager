from django.contrib import admin
from Tasks.models import Task, TaskAdmin

admin.site.register(Task,TaskAdmin)

