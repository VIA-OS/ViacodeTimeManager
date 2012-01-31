# Create your views here.
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.template import loader, Context
from Tasks.models import Task
from Tasks.models import User
from django.http import HttpResponse

@login_required()
def index(request):
    return render_to_response('index.html')

#list all tasks
def list_all_tasks(request):
    current_user = request.user.username
    tasks = Task.objects.all() #.filter(created_by=current_user)
    return render_to_response("my tasks.html", { 'tasks': tasks })

#ordering
#class Meta:
 #   ordering = ('-assigned_to_date',)