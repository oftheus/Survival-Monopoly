import random
from casa import *

class zonaPerigosa(Casa):
    def __init__(self, id, distanceToNext, name):
        super().__init__(id, distanceToNext, name)

    def ativarEvento(self, jogador):
        valores = [50, 100, 150, 200]
        valor_aleatorio = random.choice(valores)
        jogador.suprimentos -= valor_aleatorio
        return
