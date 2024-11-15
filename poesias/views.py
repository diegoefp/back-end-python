from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from faker import Faker
from .models import Book, Author, Category

# Create your views here.
def my_view(request):
    return render(request, 'sobre.html')

def user_view(request, username):
    return HttpResponse(f"Perfil do usuário: {username}")

def root_view(request):
    return HttpResponse("Estamos na raiz. porta 8000")

def home(request):
    authors = Author.objects.all()
    categories = Category.objects.all()
    
    return render(request, 'home.html', context={
        'authors': authors,
        'categories': categories
    })


def contexto(request):
    # Dados que você quer passar para o template
    context = {
        'nome': 'João',
        'idade': 30,
        'hobbies': ['Leitura', 'Ciclismo', 'Cozinhar']
    }
    return render(request, 'contexto.html', context)

def produtos_view(request):
    return render(request, 'produtos.html')

def contato_view(request):
    return render(request, 'contato.html')

def prof(request):
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


def category(request, category_id):
    books = Book.objects.filter(categories__id=category_id,)

    if not books:
        raise Http404("Not Found ")
    
    return render(request, 'category.html', context={
        'books': books,
        'title': f'Categoria: {books.first().categories.all()[0]}'
    })
    

def author(request, author_id):
    author_instance = get_object_or_404(Author, id=author_id)
    books = Book.objects.filter(author=author_instance)

    if not books:
        raise Http404("Nenhum livro encontrado para este autor.")

    return render(request, 'author.html', context={
        'books': books,
        'title': f'Autor: {author_instance.name}'
    })


def category_404(request, category_id):
    books = get_list_or_404 (Book.objects.filter(categories__id=category_id,))
    
    print("Books: ", books)
    print("Books: ", books[0])
    print("Books: ", books[0].categories.all()[0])


    return render(request, 'category404.html', context={
        'books': books,
        'title': f'Categoria: {books[0].categories.all()[0]}'
    })

def search(request):
    query = request.GET.get('query', '').strip()
    # Supondo que estamos buscando autores pelo nome
    autores = Author.objects.filter(name__icontains=query).order_by('-id')

    # Se houver autores encontrados, busque os livros do primeiro autor encontrado
    if autores.exists():
        livros = Book.objects.filter(author=autores.first())
    else:
        livros = []

    return render(request, 'search.html', {
        'first': f'Busca por "{query}"',
        'authors': autores,
        'books': livros,
    })
