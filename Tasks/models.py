import datetime
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin

class Task(models.Model):
    text = models.CharField(max_length=1024)
    description = models.TextField()
    task_create_date = models.DateTimeField(default=datetime.datetime.now())
    change_date = models.DateTimeField(blank=True)
    offsets_count = models.IntegerField(default=0)

    # 4
    author = models.ForeignKey(User, blank= True)
    importance = models.BooleanField()
    urgency = models.BooleanField()

    def __unicode__(self):
        return self.author.username
    #def __unicode__(self):
     #   return self.text

class TaskAdmin(admin.ModelAdmin):
    list_display = ('text','task_create_date')   # add grid to task list with date

    def save_model(self, request, obj, form, change):
        obj.author = request.user # no need to check for it.
        obj.save()
