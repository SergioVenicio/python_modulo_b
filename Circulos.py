class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcula_area(self):
        self.area = 3.14 * (self.raio ** 2)

    def calcula_volume(self, altura):
        self.volume = 3.14 * (self.raio ** 2) * altura
