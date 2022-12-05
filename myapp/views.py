from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def index(request):
    return HttpResponse("Index Page:")

def hello(request, id):
    return HttpResponse('<h1>Hello %s </h1>' % id)

def about(request):
    return HttpResponse('<h1>About</h1>')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe = False)

def tasks(request, id):
    task =  get_object_or_404(Task, id=id)
    return HttpResponse('tasks %s' % task.title)