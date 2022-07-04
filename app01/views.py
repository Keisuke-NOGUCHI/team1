from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def root(request):
    return HttpResponse('Hello Django')

def pattern(request, username):
    return HttpResponse('Hello {}'.format(username))

def param(request):
    text = ''
    for key in request.GET:
        text += '{} : {}, '.format(key, request.GET[key])
    return HttpResponse(text)

def top(request):
    return render(request, 'app01/top.html')

def dm(request):
    return render(request, 'app01/dm.html')

def tt(request):
    return render(request, 'app01/tt.html')

def logout(request):
    return render(request, 'app01/login.html')

def cla(request):
    return render(request, 'app01/cla.html')

def event(request):
    return render(request, 'app01/event.html')