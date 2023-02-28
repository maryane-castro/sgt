from django.shortcuts import render
from django.http import HttpResponse



def index(resquest):
    return HttpResponse('Olá, Mundo!')

def saudacoes(resquets, name):
    return HttpResponse("Nome: " + name)
# Create your views here.
