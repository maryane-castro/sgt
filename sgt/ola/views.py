from django.shortcuts import render
from django.http import HttpResponse



def index(resquest):
    return render(resquest, 'index.html')

def saudacoes(resquets, name):
    return HttpResponse(f"<h1 style='color:rgb(150, 80, 219)'>Olá {name}</h1>"  %name)
# Create your views here.
