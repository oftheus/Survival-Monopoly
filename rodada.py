from jogador import *
from turno import *

class Rodada:
    def __init__(self, id):
        self.id = id
        self.turnos = []
        return
    
    def atualizarOrdem(self,jogadores):
        for jogador in jogadores:
            self.turnos.append(Turno(jogador))