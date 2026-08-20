from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app2(request):
    return HttpResponse('second app')

def app2_me(request):
    return HttpResponse('second  app me page')