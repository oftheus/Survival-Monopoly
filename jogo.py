import pygame
import sys
from utilitario import *
from dado import *
from jogador import Jogador, JogadorSprite
from baralho import *
from jogo import *
from tabuleiro import *
from controlador import *
from controladorHumano import *
from controladorIA import*
from rodada import *
from displaylog import *

class jogo:
    def __init__(self, screen, qtd_jogadores, qtd_ia, dificuldadeAi):
        self.tabuleiro = tabuleiro([6, 10, 6, 10])

        # Inicializa os jogadores e suas posições iniciais
        self.jogadores = []
        self.posicoes_iniciais = []
        self.iniciar_jogadores(
            qtd_jogadores, self.tabuleiro.getCasa("Partida"), qtd_ia, dificuldadeAi)

        self.BGTABULEIRO = get_tabuleiro()
        # Obtém a fonte para renderizar o dinheiro dos jogadores
        self.font = get_fonte_titulo(24)

        # Criar uma instância da carta
        self.baralhoInstance = Baralho.instance()
        self.baralhoInstance.init()
        self.screen = screen
        self.dlog = DisplayLog.instance()
        self.dlog.init(self.screen, get_fonte_titulo(26))
        self.qtd_jogadores = qtd_jogadores
        self.locked = False
        self.rodadas = []
        self.jogar()

    def criaRodada(self):
        self.rodadaAtual = Rodada(self.turnId)
        self.rodadaAtual.atualizarOrdem(self.jogadores)
        self.turnId+=1            
        self.rodadas.append(self.rodadaAtual)

    # funcão principal para o jogo
    def jogar(self):
        self.currentPlayerid = 0
        self.currentPlayer = self.jogadores[self.currentPlayerid]
        self.turnId = 0
        self.criaRodada()
        # GAME LOOP
        while True:
            # Desenha display
            self.draw_graphics()
            
            self.currentPlayer = self.rodadaAtual.turnos[self.currentPlayerid].getJogador()

            # Faz o turno
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.currentPlayer.controlador.awaitsInput():
                        if event.button == 1 and not self.locked:
                           self.fazerTurnoJogador(event)
                    elif not self.locked: #Ainda espera um click para passar turno da IA
                        self.fazerTurnoJogador(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.currentPlayer.suprimentos < 0:
                self.currentPlayer.transforma_zumbi()

            jogadores_ativos = [j for j in self.jogadores if not j.isZombie()]
            if len(jogadores_ativos) == 1:
                if self.exibir_tela_final(jogadores_ativos[0]):
                    self.__init__(self.screen, self.qtd_jogadores)
                else:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

    def fazerTurnoJogador(self, event):
        roll = sprite_dado.rolar()
        roll += sprite_dado2.rolar()
        self.tabuleiro.iterarCasas(
            self.currentPlayer, roll)

        # Passa o turno para o próximo jogador
        self.currentPlayerid += 1
        if self.currentPlayerid > len(self.rodadaAtual.turnos) -1:
            self.currentPlayerid = 0
            self.criaRodada()

    def exibir_tela_final(self, jogador_vencedor):
        self.screen.fill((0, 0, 0))  # Preenche a tela com a cor preta
        # Pega a fonte para a mensagem de vitória
        fonte_vencedor = get_fonte_titulo(80)
        texto_vencedor = fonte_vencedor.render(
            f'Jogador {(jogador_vencedor.id)+1} Sobreviveu!', True, (255, 255, 255))
        # Desenha a mensagem de vitória
        self.screen.blit(texto_vencedor, (350, 300))

        # Desenha botao de "Sair"
        fonte_botoes = get_fonte_titulo(30)
        texto_sair = fonte_botoes.render('Sair', True, (255, 255, 255))
        rect_sair = texto_sair.get_rect(center=(600, 600))
        self.screen.blit(texto_sair, rect_sair.topleft)

        pygame.display.update()

        # Espera a interação do usuário
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clique esquerdo do mouse
                        if rect_sair.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()

    # função para a interface gráfica

    def draw_graphics(self):
        # Desenha o fundo do tabuleiro na tela
        self.screen.blit(self.BGTABULEIRO, (0, 0))
        # desenha os peoes na tela do jogo
        for jogador in self.jogadores:
            jsprite = jogador.peca.jogadorSprite
            self.screen.blit(jsprite.imagem, jsprite.rect)

        # desenhar o dinheiro dos jogadores
        for jogador in self.jogadores:
            if jogador.id != self.currentPlayerid:
                jogador.renderizar_suprimento(self.font, self.screen, (0,0,0))
            else:
                jogador.renderizar_suprimento(self.font, self.screen, (97,19,11))


        self.tabuleiro.exibir_info_casa(self.screen)
        self.dlog.displayLog()        
        # Desenha o dado na tela
        sprite_dado.draw(self.screen)
        sprite_dado2.draw(self.screen)

        self.baralhoInstance.draw(self.screen)

        # Atualiza a tela do jogo
        pygame.display.update()

    def iniciar_jogadores(self, qtd_jogadores, casaInicial, qtd_ia, dificuldadeIA = 1):
        peao_info = [("assets/peao1.png", (8, 670), (40, 45)),  # (x,y) , (largura, altura)
                     ("assets/peao2.png", (58, 670), (40, 49)),
                     ("assets/peao3.png", (108, 670), (40, 40)),
                     ("assets/peao4.png", (8, 750), (40, 28)),
                     ("assets/peao5.png", (58, 750), (40, 33)),
                     ("assets/peao6.png", (108, 740), (40, 49))]
        baseCoordX = 58
        baseCoordY = 700
        yDeviation = 11
        xDeviation = 6
        controladores = []
        for i in range(0,qtd_jogadores):
            if i < qtd_ia:
                controladores.append(
                    IA(dificuldadeIA, self)
                )
            else:
                controladores.append(Humano(self))
        self.posicoes_iniciais = [(baseCoordX, baseCoordY),
                                  (baseCoordX + xDeviation, baseCoordY+yDeviation),
                                  (baseCoordX - xDeviation, baseCoordY-yDeviation),
                                  (baseCoordX + xDeviation, baseCoordY+yDeviation),
                                  (baseCoordX, baseCoordY-yDeviation),
                                  # Posições iniciais para cada jogador
                                  (baseCoordX - xDeviation, baseCoordY)]
        # 58,700
        for i in range(qtd_jogadores):
            jogador = Jogador(controladores[len(controladores)-i-1],i, casaInicial, JogadorSprite(
                peao_info[i][0], peao_info[i][2], self.posicoes_iniciais[i]),self.tabuleiro)
            # Atribui o caminho da imagem do peão e o tamanho com base em peao_info
            self.jogadores.append(jogador)

    def lock(self):
        self.draw_graphics()
        self.locked = True
    
    def unlock(self):
        self.locked = False




