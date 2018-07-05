class Animal:
    vivo = True

    def comer(self):
        print(f'Comendo {self.alimento}...')


class AnimalDomestico(Animal):
    habitat = 'domestico'


class AnimalSelvagem(Animal):
    habitat = 'selva'


class Carnivoro(Animal):
    alimento = 'carne'


class Tigre(Carnivoro, AnimalSelvagem):
    def comer(self, alimento):
        alimento.vivo = False

        try:
            print(f'Comendo {alimento.nome} ...')
        except AttributeError:
            print(f'Comendo {self.alimento} ...')


class Cachorro(Carnivoro, AnimalDomestico):
    cobertura = 'pelos'
    patas = 4

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self, vezes):
        print('uau ' * vezes)


class Galinha(AnimalDomestico):
    cobertura = 'penas'
    alimento = 'grãos'
    patas = 2
    bico = 'pequeno'
