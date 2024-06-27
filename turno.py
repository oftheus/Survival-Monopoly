from jogador import *

class Turno:
    def __init__(self, jogador):
        self.jogador = jogador
        self.jogada = ""

    def getJogador(self):
        return self.jogador

    def salvaJogada(self, jogada): 
        self.jogada = jogada

    def getJogada(self, jogada): 
        self.jogada = jogada