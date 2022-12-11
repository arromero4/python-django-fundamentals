from django.shortcuts import render, get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject
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
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    #return JsonResponse(projects, safe = False)
    return render(request, 'projects.html',{
        'projects': projects
    })

def tasks(request):
    #task =  get_object_or_404(Task, id=id)
    #return HttpResponse('tasks %s' % task.title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        #SHOW INTERFACE
        return render(request, 'create_task.html',{
                'form': CreateNewTask()
                })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request,'create_project.html', {
        'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'detail.html',{
        'project': project,
        'tasks': tasks,
    })