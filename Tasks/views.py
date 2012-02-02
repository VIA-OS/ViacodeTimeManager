# Create your views here.
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.template import loader, Context
from django.template.context import RequestContext
from Tasks.models import Task
from Tasks.models import User
from django.http import HttpResponse

@login_required()
def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

#list all tasks
def list_all_tasks(request):
    current_user = request.user
    tasks = Task.objects.filter(created_by=current_user.id)
    return render_to_response("tm.tasks.html", { 'tasks': tasks }, context_instance=RequestContext(request))

#ordering
#class Meta:
 #   ordering = ('-assigned_to_date',)y