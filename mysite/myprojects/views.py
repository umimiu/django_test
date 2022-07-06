from django.shortcuts import render
from django.http import HttpResponse
from . models import Project


def hello(request):
    return HttpResponse('<h1>Page my projects</h1>')
    # return render(request, 'hello.html')


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'title': 'My Projects',
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
        'title': 'About Project',
    }
    return render(request, 'project_detail.html', context)
