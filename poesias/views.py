from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def my_view(request):
    return render(request, 'sobre.html')

def user_view(request, username):
    return HttpResponse(f"Perfil do usuário: {username}")

def root_view(request):
    return HttpResponse("Estamos na raiz. porta 8000")

def contexto(request):
    context ={
        'nome': 'joão',
        'idade': 30,
        'hobbies': ['Leitura', 'Ciclismo', 'Cozinhar']
    }
    return render(request, 'contexto.html', context)

def produtos(request):
    return render(request, 'produtos.html')

def contato(request):
    return render(request, 'contato.html')

def professor(request):
    return render(request, 'professor.html')