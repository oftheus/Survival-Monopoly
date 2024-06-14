from casa import *
from assentamento import *
from emboscada import *
from encurralado import *
from pontoPartida import *
from portoSeguro import *
from terraDeNinguem import *
from zonaPerigosa import *

class tabuleiro:
    def __init__(self, noCasas):
        self.id = id
        self.casas = []
        #Cria casas, de modo que a distancia gráfica entre elas seja consistente
        dx = 100 #valores das distancias entre as casas
        dy = -100
        horizontal = False 
        direction = 1
        casasEspeciais = [ #Casas que ficam na borda do tabuleiro
            pontoPartida(0, [0,-120], "Partida"),
            Emboscada(noCasas[0], [125,-10], "Partida"),
            PortoSeguro(noCasas[0] + noCasas[1], [0,120], "Partida"),
            Encurrlada(noCasas[0] + noCasas[1] + noCasas[2], [-125,10], "Partida"),
        ]
        for i in range(0,len(noCasas)):
            self.casas.append(casasEspeciais[i])
            for j in range(0, noCasas[i]-1):
                dVec = [0, direction*dy]
                if horizontal:
                    dVec = [direction*dx, 0]
                novaCasa = Assentamento(len(self.casas),dVec, "casa", 200)  #no momento, todas sao assentamentos
                #posteriormente, dividir assentamentos em grupos
                
                self.casas.append(novaCasa) #add novas infos a casa posteriormente
            horizontal = not horizontal
            if not horizontal:
                direction = direction * (-1)
            

    def getCasa(self,casaAlvo):
        for casa in self.casas:
            if casa.name == casaAlvo:
                return casa
            
    def iterarCasas(self, jogador, qtdCasas):
        for i in range(0,qtdCasas):
            #print(jogador.peca.casa.id)
            #print("prox casa ideal: ",(jogador.peca.casa.id + 1) % len(self.casas))
            #print("prox casa: ",self.casas[(jogador.peca.casa.id + 1) % len(self.casas)].id)
            #print(jogador.peca.casa.distanceToNext)

            newPosX = jogador.peca.jogadorSprite.rect.topleft[0] + jogador.peca.casa.distanceToNext[0]
            newPosY = jogador.peca.jogadorSprite.rect.topleft[1] + jogador.peca.casa.distanceToNext[1]
            jogador.peca.jogadorSprite.rect.topleft = [newPosX, newPosY]
            jogador.peca.casa = self.casas[(jogador.peca.casa.id + 1) % len(self.casas)]

        jogador.peca.casa.ativarEvento(jogador)
