from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def index(request):
    title = 'Welcome to Django course!!'
    return render(request,'index.html', {
        'title': title,
    })

def about(request):
    username = 'ARROMERO'
    return render(request, 'about.html', {
        'username': username
    })

def hello(request, id):
    return HttpResponse('<h1>Hello %s </h1>' % id)



def projects(request):
    projects = list(Project.objects.values())
    #return JsonResponse(projects, safe = False)
    return render(request, 'projects.html',{
        'projects': projects
    })

def tasks(request, id):
    #task =  get_object_or_404(Task, id=id)
    #return HttpResponse('tasks %s' % task.title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })