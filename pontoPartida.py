from casa import *
class pontoPartida(Casa):
    def __init__(self, id, distanceToNext, name):
        super().__init__(id, distanceToNext, name)

    def ativarEvento(self, jogador): #fzr overload desse compartamento pra cada subclasse
        jogador.suprimentos = jogador.suprimentos + 600
        return