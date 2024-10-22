from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker

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

def pextends(request):
    return render(request, 'page_extends.html')

fake = Faker('pt_BR')

def make_poetry():
    return{
        'title': fake.sentence(nb_words=5),
        'full_text': fake.text(250),
        'created_at': fake.date_time(),
        'author':{
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'genre':{
            'name': fake.word()
        },
        'cover':{
            'url': 'https://loremflickr.com/320/320/poetry,book',
        },
        'is_popular': fake.boolean()
    }


def poema_detail(request):
    poetry = make_poetry()
    return render(request, 'poema_detail.html', {'poetry': poetry})