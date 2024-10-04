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
from django.urls import path
from poesias.views import my_view, user_view, root_view, home, contexto, produtos, contato, professor

urlpatterns = [
    path('', root_view),
    path('home/', home),
    path('sobre/', my_view),
    path('user/<str:username>/', user_view),
    path('contexto/', contexto),
    path('produtos/', produtos),
    path('contato/', contato),
    path('professor/', professor),
    
]
