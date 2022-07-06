from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('<h1>Page about</h1>')
    # return render(request, 'about.html')


def home(request):
    return HttpResponse('<h1>Page home</h1>')
    # return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['username']
    return render(request, 'reverse.html', {'word': user_text[::-1]})