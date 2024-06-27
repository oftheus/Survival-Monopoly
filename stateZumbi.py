from stateJogador import *
class ZumbiState(JogadorState):
    def __init__(self):
        return

    def isZombie(self): return True

    def atualizarSuprimentos(self,jogador, s):
        if s<0:
            if jogador.controlador.controlar("Pilhar Base"):
                return -s*2
        return 0