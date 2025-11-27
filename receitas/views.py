#views.py responsável pelas funções a serem retornadas nas paginas
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #Importei o HttpResponse do Django

def home(request):
    return render(request, "home.html", context={'nome': 'Receitas Django'}) 

def sobre(request):
    return HttpResponse("Sobre nós")#Usei o HttpResponse

def receita(request):
    return HttpResponse("Receitas") 