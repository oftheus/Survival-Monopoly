from casa import *
from tituloAssentamento import *

class Assentamento(Casa):
    def __init__(self, id, distanceToNext, name, titulo):
        super().__init__(id, distanceToNext, name)
        self.titulo = titulo
        self.titulo.casa = self
        self.fortalezas = 0

    def ativarEvento(self, jogador): #fzr overload desse compartamento pra cada subclasse
        if not self.titulo.comprado:
            self.comprar(jogador)
        else:
            if jogador != self.titulo.jogador:
                #tira valor igual ao custo do jogador que caiu na casa, da pro dono
                jogador.modificarSuprimentos(-self.titulo.custo)
                self.titulo.jogador.modificarSuprimentos(+self.titulo.custo)
            else:
                if self.titulo.grupo.verificarPosseGrupo(jogador):
                    self.construirFortaleza(jogador)
    
    def comprar(self,jogador):
        jogador.modificarSuprimentos(-self.titulo.custo*1)
        self.titulo.atribuirAJogador(jogador)
        jogador.ganharTitulo(self.titulo)

    def construirFortaleza(self,jogador):
        jogador.modificarSuprimentos(-self.titulo.custo*1)
        self.fortalezas+=1
        self.titulo.custo *= 2

    def drawCasa(self, coord, fonte, fonteFortaleza, screen): #deve ser implementado na casa
        #Ajusta texto para ficar bonito (dependendo da casa em questão):
        if self.distanceToNext[1] < -70:
            coord[0] -=10
            coord[1] -=10
        if self.distanceToNext[1] > 70:
            coord[0] +=36
            coord[1] -=20
        if self.distanceToNext[0] > 70:
            coord[1] -=6
        if self.distanceToNext[0] < -70:
            coord[1] +=3
        if self.id>10 and self.id<16:
            coord[0] += 3 + (self.id-12)/1
        coord[1] -= 10

        #Dependendo do estado da casa, mostra informações
        if self.titulo.jogador == None:
            textoCasa = fonte.render(
                    f'    Sem dono  ', True, (255, 255, 255))
        else:    
            if not self.titulo.jogador.isZombie():
                textoCasa = fonte.render(
                        f'  Do jogador ' + str(self.titulo.jogador.id+1) + ' ', True, (255, 255, 255))
            else:
                textoCasa = fonte.render(
                        f' Horda zumbi  ', True, (255, 255, 255))
        #Se tem fortalezas, desenha
        if self.fortalezas>0:
            textoFortaleza = fonteFortaleza.render(
                    f'  Fortalezas: ' + str(self.fortalezas) + ' ', True, (255, 255, 255))
        
        # Desenha a info
        screen.blit(textoCasa, coord)