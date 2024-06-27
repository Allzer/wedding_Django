from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Главная страница')

def cat(request):
    return HttpResponse('cat')