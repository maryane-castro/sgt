from django.shortcuts import render
from django.http import HttpResponse



def index(resquest):
    return render(resquest, 'index.html')



def greet(resquest, name):
    return render(resquest, 'greet.html', {'name':name})


"""def saudacoes(resquets, nome):
    return HttpResponse(f"<h1 style='color:rgb(150, 80, 219)'>Olá {nome}</h1>"  %nome)
# Create your views here."""
