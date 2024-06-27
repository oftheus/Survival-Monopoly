from stateJogador import *
class ZumbiState(JogadorState):
    def __init__(self):
        return

    def isZombie(self): return True

    def atualizarSuprimentos(self,jogador, s):
        print('ataque zumbi')
        return -s*2