from casa import *
class Emboscada(Casa):
    def __init__(self, id, distanceToNext, name):
        super().__init__(id, distanceToNext, name)

    def ativarEvento(self, jogador): #fzr overload desse compartamento pra cada subclasse
        if not jogador.usarCartaDistracao():
            jogador.encurrala() #envia jogador pra prisão