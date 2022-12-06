from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def hello(request, id):
    return HttpResponse('<h1>Hello %s </h1>' % id)



def projects(request):
    projects = list(Project.objects.values())
    #return JsonResponse(projects, safe = False)
    return render(request, 'projects.html')

def tasks(request, id):
    task =  get_object_or_404(Task, id=id)
    #return HttpResponse('tasks %s' % task.title)
    return render(request, 'tasks.html')