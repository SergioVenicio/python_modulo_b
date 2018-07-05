from random import randint
from Animais import Cachorro

matilha = []
[matilha.append(Cachorro(f'j{i}', randint(1, 20))) for i in range(1, 101)]
for cachorro in matilha:
    print(f'Nome: {cachorro.nome}, idade: {cachorro.idade}')
