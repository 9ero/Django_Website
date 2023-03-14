from django.http import HttpResponse, JsonResponse
from .models import Task, Project
from django.shortcuts import get_object_or_404, render
# Create your views here.
def holaMundo(request):
    return render(request, 'index.html')

def names(request, username):
    return HttpResponse("<h3>Hola %s</h3>" %username)

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    #if id is not found return a 404 instead of an error
    task=get_object_or_404(Task, id=id)
    
    return HttpResponse('Task:  %a' % task.description)