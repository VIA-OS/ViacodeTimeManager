import datetime
from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin

class Task(models.Model):
    task_title = models.CharField(max_length=1024)
    description = models.TextField(blank=True)
    task_create_date = models.DateTimeField(default=datetime.datetime.now())
    change_date = models.DateTimeField(blank=True)
    assigned_to_date = models.DateField(blank=True)
    offsets_count = models.IntegerField(default=0)
    # 4
    created_by = models.ForeignKey(User, related_name="Created By")
    importance = models.BooleanField()
    urgency = models.BooleanField()

    #def __unicode__(self):
     #   return self.text

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title','task_create_date')   # add grid to task list with date

    #code below f or automate filling created_by field with current user name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
            if db_field.name == 'created_by':
                kwargs['queryset'] = User.objects.filter(username=request.user.username)
            return super(TaskAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ('created_by',)
        return self.readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data['created_by'] = request.user
        request.GET = data
        return super(TaskAdmin, self).add_view(request, form_url, extra_context=extra_context)