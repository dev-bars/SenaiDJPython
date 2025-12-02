#Importação das bibliotecas
from random import randint
from faker import Faker

falso = Faker('pt-BR')

def randomicos():
    return randint(840,900), randint(473,573)

def gen_fake_receita():
    receita = {
        'titulo': falso.sentence(nb_words=4),
        'descricao': falso.paragraph(nb_sentences=3),
        'tempo_preparo': falso.random_number(digits=2, fix_len=True),
        'unidade_tempo': 'minutos',
        'porcoes': falso.random_number(digits=1, fix_len=True),
        'passos_preparo': falso.text(3000),
        'Data_publicacao': falso.date_between(start_date='-1y', end_date='today'),
        'autor':{
            'nome': falso.name(),
            'sobrenome': falso.last_name(),
        },
        'imagem': 'http://loremflickr.com/%s/%s/food,cook&#39' % randomicos()
    }

    return receita
if __name__ == "__main__":
    from pprint import pprint
    pprint(gen_fake_receita())