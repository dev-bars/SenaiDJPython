#urls.py (receitas) responsável por gerenciar o caminho das paginas
from django .urls import path
from .views import home, sobre, receita

urlpatterns = [
    path("", home),
    path("sobre/", sobre),
    path("receitas/", receita),
]