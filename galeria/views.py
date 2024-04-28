from django.shortcuts import render
from django.http import HttpResponse #faz e responde uma requisicao
#Cuidar do que será exibo em cada tela

def index(request):
    return render(request,'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')