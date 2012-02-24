# Create your views here.
from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from django.template import loader, Context
from django.template.context import RequestContext
from Tasks.models import Task
from Tasks.models import User
from django.template.loader import get_template
from django.http import HttpResponse
from django.core import serializers

@login_required()
def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

#list all tasks
def list_all_tasks(request):
    current_user = request.user
    tasks = Task.objects.filter(created_by=current_user.id)
    return render_to_response("tm.tasks.html", { 'tasks': tasks }, context_instance=RequestContext(request))

#list all tasks ajax
def list_tasks_ajax(request):
    current_user = request.user
    data = ""
    if request.is_ajax():
        task_filter = request.GET.get('task_by_date_filter')
        #t = get_template("tm.tasks.html")
        tasks = Task.objects.filter(assigned_to_date=task_filter)
        #html = t.render({ 'tasks': tasks })
        data = serializers.serialize("json",tasks)
    elif request.method == 'POST':
        print request.POST
    return HttpResponse(data)