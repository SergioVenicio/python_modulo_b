from random import random


class Sprites:
    def __init__(self, nome, tamanho='grande', cor='amarelo', arestas=5):
        self.nome = nome
        self.tamanho = tamanho
        self.cor = cor
        self.arestas = arestas

    def update_position(self):
        self.position = random() * 10, random() * 10
        print(f'{self.nome} está agora em {self.position}')
