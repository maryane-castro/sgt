from django.shortcuts import render
from django.http import HttpResponse



def index(resquest):
    return HttpResponse('Olá, Mundo!')


# Create your views here.
