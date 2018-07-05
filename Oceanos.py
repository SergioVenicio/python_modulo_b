class Atlantico:
    carater1 = 'É um oceano'


class Indico:
    carater2 = 'perigoso, '


class Pacifico(Indico):
    carater3 = 'cheio de tsunamis '


class Artico(Atlantico, Indico, Pacifico):
    carater4 = 'e muito gelado!'
