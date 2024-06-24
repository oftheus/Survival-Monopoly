from casa import *
class Assentamento(Casa):
    def __init__(self, id, distanceToNext, name, custo):
        super().__init__(id, distanceToNext, name)
        self.custo = custo

    def ativarEvento(self, jogador): #fzr overload desse compartamento pra cada subclasse
        jogador.suprimentos -= self.custo
        return