from casa import *
from assentamento import *
from emboscada import *
from encurralado import *
import math
from utilitario import *
from pontoPartida import *
from portoSeguro import *
from terraDeNinguem import *
from zonaPerigosa import *
from grupoAssentamento import *


class tabuleiro:
    def __init__(self, noCasas):
        self.id = id

        #inicia titulos de assentamento
        self.gruposAssentamento = [
            GrupoAssentamento("vermelho", 3),
            GrupoAssentamento("azul", 3),    
            GrupoAssentamento("rosa", 3),    
            GrupoAssentamento("laranja", 3),    
            GrupoAssentamento("verde", 3),    
            GrupoAssentamento("amarelo", 3),    

        ]

        self.custosAssentamentos = [70,70,100,140,160,140,180,200,200,220,240,280,300,300,320,200,350,400]

        self.casas = []
        # Cria casas, de modo que a distancia gráfica entre elas seja consistente
        dx = 99.2  # valores das distancias entre as casas
        dy = -100
        qtdAssentamentos = 0
        horizontal = False
        direction = 1
        casasEspeciais = [  # Casas que ficam na borda do tabuleiro
            pontoPartida(0, [-15, -120], "Partida"),
            Emboscada(noCasas[0], [136, -10], "Emboscada"),
            PortoSeguro(noCasas[0] + noCasas[1], [15, 120], "PortoSeguro"),
            Encurrlada(noCasas[0] + noCasas[1] + \
                       noCasas[2], [-110, 10], "Encurralada"),
        ]
        for i in range(0, len(noCasas)):
            self.casas.append(casasEspeciais[i])
            for j in range(0, noCasas[i]-1):

                dVec = [0, direction*dy]
                if horizontal:
                    dVec = [direction*dx, 0]
                # no momento, todas sao assentamentos
                if (i == 0 and j == 1) or (i == 1 and j == 1) or (i == 1 and j == 7) or (i == 2 and j == 4) or (i == 3 and j == 4):
                    novaCasa = zonaPerigosa(len(self.casas), dVec, "zona de perigo")
                elif (i == 0 and j == 3) or (i == 1 and j == 4) or (i == 2 and j == 2) or (i == 3 and j == 2) or (i == 3 and j == 7):
                    novaCasa = TerraDeNinguem(len(self.casas), dVec, "terraDeNinguem")
                else:
                    novoTitulo = Titulo(self.custosAssentamentos[qtdAssentamentos])
                    novaCasa = Assentamento(len(self.casas), dVec, "casa", novoTitulo)
                    # add nova aoo grupo
                    #print('create assentamento, grupo:', math.floor(len(self.casas)/3))
                    self.gruposAssentamento[math.floor(qtdAssentamentos//3)].inserirCasa(novaCasa)
                    qtdAssentamentos+=1

                self.casas.append(novaCasa)
            horizontal = not horizontal
            if not horizontal:
                direction = direction * (-1)
        #for ga in self.gruposAssentamento:
        #    ga.printSelf()
                
    def getCasa(self, casaAlvo):
        for casa in self.casas:
            if casa.name == casaAlvo:
                return casa

    def iterarCasas(self, jogador, qtdCasas):
        for i in range(0, qtdCasas):
            # print(jogador.peca.casa.id)
            # print("prox casa ideal: ",(jogador.peca.casa.id + 1) % len(self.casas))
            # print("prox casa: ",self.casas[(jogador.peca.casa.id + 1) % len(self.casas)].id)
            # print(jogador.peca.casa.distanceToNext)

            newPosX = jogador.peca.jogadorSprite.rect.topleft[0] + \
                jogador.peca.casa.distanceToNext[0]
            newPosY = jogador.peca.jogadorSprite.rect.topleft[1] + \
                jogador.peca.casa.distanceToNext[1]
            jogador.peca.jogadorSprite.rect.topleft = [newPosX, newPosY]
            jogador.peca.casa = self.casas[(
                jogador.peca.casa.id + 1) % len(self.casas)]
            if jogador.peca.casa.name == "Partida":
                #dar dinheiro por passar em partida?
                #atualiza pos de volta pra pos inicial (p/evitar que pos muda com loop)
                jogador.peca.jogadorSprite.rect.topleft = [50,700]

        jogador.peca.casa.ativarEvento(jogador)

    def getCasaCoord(self, casa):
        casaId = casa.id
        posX = 50
        posY = 700
        for i in range(0, casaId):
            posX = posX + self.casas[i].distanceToNext[0]
            posY = posY + self.casas[i].distanceToNext[1]
        return [posX,posY]
    

    
    def exibir_info_casa(self, screen):
        # Pega a fonte 
        fonte = get_fonte_titulo(15)
        fonteFortaleza = get_fonte_titulo(10)
        for casa in self.casas:
            casa.drawCasa(self.getCasaCoord(casa), fonte, fonteFortaleza, screen)

        #pygame.display.update()
       