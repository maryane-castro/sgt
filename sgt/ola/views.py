from django.shortcuts import render
from django.http import HttpResponse



def index(resquest):
    return HttpResponse('Olá, Mundo!')

def saudacoes(resquets, name):
    return HttpResponse(f"<h1 style='color:rgb(150, 80, 219)'>Olá {name}</h1>")
# Create your views here.
