import pygame, sys
from utilitario import *
from dado import *
from jogador import Jogador, JogadorSprite
from carta import *
from jogo import *
from tabuleiro import *

class jogo:
    def __init__(self, screen, qtd_jogadores):
        self.tabuleiro = tabuleiro([6, 10, 6, 10])
        
         # Inicializa os jogadores e suas posições iniciais
        self.jogadores=[]
        self.posicoes_iniciais = []
        self.iniciar_jogadores(qtd_jogadores, self.tabuleiro.getCasa("Partida"))

        self.BGTABULEIRO = get_tabuleiro()
        # Obtém a fonte para renderizar o dinheiro dos jogadores
        self.font = get_fonte_titulo(24)

        # Criar uma instância da carta
        self.cartaSprite = Carta()

        self.screen= screen
        self.qtd_jogadores = qtd_jogadores

        self.jogar()

    #funcão principal para o jogo
    def jogar(self):
        self.currentPlayerid = 0
        self.currentPlayer = self.jogadores[self.currentPlayerid]
        # GAME LOOP
        while True:
            # Desenha display
            self.draw_graphics()
            self.currentPlayer = self.jogadores[self.currentPlayerid]

            # Faz o turno
            #Await roll input:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN: # Quando um botão do mouse é pressionado
                    if event.button == 1: # Botão esquerdo do mouse                            if sprite_dado.rect.collidepoint(event.pos): # Verifica se o botão do dado foi clicado
                        roll = sprite_dado.rolar() # Rola o dado
                        self.tabuleiro.iterarCasas(self.currentPlayer, roll)
                        
                        #passa o turno para o prox jogador
                        self.currentPlayerid += 1
                        self.currentPlayerid = self.currentPlayerid % len(self.jogadores)
                if event.type == pygame.QUIT: # Botão direito do mouse ( TIRAR ISSO DEPOIS )
                    pygame.quit() # Fecha o pygame
                    sys.exit() 
            
            if self.currentPlayer.suprimentos < 0:
                self.currentPlayer.transforma_zumbi()
                amountOfZombies = 0
                for jogador in self.jogadores:
                    if jogador.isZombie():
                        amountOfZombies += 1
                if amountOfZombies == len(self.jogadores) -1 :
                    pygame.quit() # Fecha o pygame
                    sys.exit() 
            
        

    #função para a interface gráfica
    def draw_graphics(self):
            self.screen.blit(self.BGTABULEIRO, (0, 0)) # Desenha o fundo do tabuleiro na tela
            # desenha os peoes na tela do jogo
            for jogador in self.jogadores:
                jsprite = jogador.peca.jogadorSprite
                self.screen.blit(jsprite.imagem, jsprite.rect)

            # desenhar o dinheiro dos jogadores
            for jogador in self.jogadores:
                jogador.renderizar_suprimento(self.font, self.screen)

            # Desenha o dado na tela
            sprite_dado.draw(self.screen)

            self.cartaSprite.draw(self.screen)

            # Atualiza a tela do jogo
            pygame.display.update()

    def iniciar_jogadores(self, qtd_jogadores, casaInicial):
        peao_info = [("assets/peao1.png", (8, 670), (40, 45)), # (x,y) , (largura, altura)
                    ("assets/peao2.png", (58, 670), (40, 49)),
                    ("assets/peao3.png", (108, 670), (40, 40)),
                    ("assets/peao4.png", (8, 750), (40, 28)),
                    ("assets/peao5.png", (58, 750), (40, 33)),
                    ("assets/peao6.png", (108, 740), (40, 49))]
        baseCoordX = 58
        baseCoordY = 700
        yDeviation = 11
        xDeviation = 6
        self.posicoes_iniciais = [(baseCoordX, baseCoordY), 
                                  (baseCoordX +xDeviation, baseCoordY+yDeviation), 
                                  (baseCoordX -xDeviation, baseCoordY-yDeviation), 
                                  (baseCoordX +xDeviation, baseCoordY+yDeviation),
                                  (baseCoordX, baseCoordY-yDeviation), 
                                  (baseCoordX -xDeviation, baseCoordY)]  # Posições iniciais para cada jogador
        #58,700
        for i in range(qtd_jogadores):
            jogador = Jogador(i, casaInicial, JogadorSprite(peao_info[i][0], peao_info[i][2], self.posicoes_iniciais[i]))
            # Atribui o caminho da imagem do peão e o tamanho com base em peao_info
            self.jogadores.append(jogador)