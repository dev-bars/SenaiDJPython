#urls.py (receitas) responsável por gerenciar o caminho das paginas
from django .urls import path
from .views import home

urlpatterns = [
    path("", home),
]