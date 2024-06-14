from casa import *
from jogador import *

class Peca:
    def __init__(self, casa, jogadorSprite):
        self.atualizarPosicao(casa)
        self.jogadorSprite = jogadorSprite
        return
    
    def atualizarPosicao(self, casa):
        self.casa = casa
    
    def getPosicao(self, casa):
        return self.casa