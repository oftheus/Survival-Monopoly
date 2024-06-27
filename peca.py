from casa import *
from jogador import *
from tabuleiro import *

class Peca:
    def __init__(self, casa, jogadorSprite, tabuleiro):
        self.atualizarPosicao(casa)  # Inicializa a posição da peça na casa fornecida
        self.jogadorSprite = jogadorSprite  # Atribui o sprite do jogador à peça
        self.tabuleiro = tabuleiro  # Atribui o tabuleiro à peça
        return

    def atualizarPosicao(self, casa):
        self.casa = casa  # Atualiza a posição da peça para a casa fornecida

    def getPosicao(self):
        return self.casa  # Retorna a posição atual da peça

    def enviaPraPrisão(self):
        casaPrisao = self.tabuleiro.getCasa("Encurralada")  # Obtém a casa de prisão do tabuleiro
        self.atualizarPosicao(casaPrisao)  # Atualiza a posição da peça para a casa de prisão
        self.jogadorSprite.rect.topleft = self.tabuleiro.getCasaCoord(casaPrisao)  # Atualiza a posição do sprite do jogador para a coordenada da casa de prisão no tabuleiro
