from casa import *
class Encurrlada(Casa):
    def __init__(self, id, distanceToNext, name):
        super().__init__(id, distanceToNext, name)

    def ativarEvento(self, jogador): #fzr overload desse compartamento pra cada subclasse
        return #Não faz nada SE o jogador está 'passando na prisão'