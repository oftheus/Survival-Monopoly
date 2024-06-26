from casa import *
from jogador import *
from tabuleiro import *

class Peca:
    def __init__(self, casa, jogadorSprite, tabuleiro):
        self.atualizarPosicao(casa)
        self.jogadorSprite = jogadorSprite
        self.tabuleiro = tabuleiro
        return
    
    def atualizarPosicao(self, casa):
        self.casa = casa
    
    def getPosicao(self, casa):
        return self.casa

    def enviaPraPrisão(self):
        print('nevio prisao')
        casaPrisao = self.tabuleiro.getCasa("Encurralada")
        self.atualizarPosicao(casaPrisao)
        self.jogadorSprite.rect.topleft = self.tabuleiro.getCasaCoord(casaPrisao)