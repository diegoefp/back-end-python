"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from poesias.views import my_view, root_view, user_view, home, contexto, produtos_view, contato_view, prof, pextends, poema_detail, category, author, category_404, search

urlpatterns = [
    path('home/', home),
    path('', root_view),
    path('sobre/', my_view),    
    path('user/<str:username>/', user_view),
    path('contexto/', contexto),
    path('produtos/', produtos_view),
    path('contato/', contato_view),
    path('prof/', prof),
    path('page_extends/', pextends),
    path('poema_detail/', poema_detail),
    path('poemas/categorias/<int:category_id>', category, name='category_id'),
    path('poemas/autor/<int:author_id>/', author, name='author_id'),
    path('poemas/categorias404/<int:category_id>', category_404, name='category_id'),
    path('search/', search, name='search'),
      
    
]
