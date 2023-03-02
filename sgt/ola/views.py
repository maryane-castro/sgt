from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(resquest):
    return render(resquest, 'index.html')



def greet(resquest, name):
    return render(resquest, 'greet.html', {'name':name})


def tiaZap(resquest, name):
    aux = datetime.datetime.now()
    dia = int(aux.strftime('%H'))
    booleano = bool
    if dia < 17:
        booleano = False
    else:
        booleano = True
    
    return render(resquest, 'tiaDoZap.html', {'name':name, 'dia': booleano})

"""def saudacoes(resquets, nome):
    return HttpResponse(f"<h1 style='color:rgb(150, 80, 219)'>Olá {nome}</h1>"  %nome)
# Create your views here."""

