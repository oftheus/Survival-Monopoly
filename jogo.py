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
from controladorIA import *
from rodada import *
from displaylog import *


class jogo:
    def __init__(self, screen, qtd_jogadores, qtd_ia, dificuldadeAi):
        # Inicializa o tabuleiro com as dimensões especificadas
        self.tabuleiro = tabuleiro([6, 10, 6, 10])

        # Inicializa a lista de jogadores e suas posições iniciais
        self.jogadores = []
        self.posicoes_iniciais = []
        self.iniciar_jogadores(
            qtd_jogadores, self.tabuleiro.getCasa("Partida"), qtd_ia, dificuldadeAi)

        # Carrega a imagem do tabuleiro
        self.BGTABULEIRO = get_tabuleiro()
        # Obtém a fonte para renderizar o dinheiro dos jogadores
        self.font = get_fonte_titulo(24)

        # Cria uma instância do baralho e inicializa
        self.baralhoInstance = Baralho.instance()
        self.baralhoInstance.init()

        # Configurações da tela e log de exibição
        self.screen = screen
        self.dlog = DisplayLog.instance()
        self.dlog.init(self.screen, get_fonte_titulo(26))
        self.qtd_jogadores = qtd_jogadores
        self.locked = False
        self.rodadas = []

        # Inicia o jogo
        self.jogar()

    def criaRodada(self):
        # Cria uma nova rodada e atualiza a ordem dos jogadores
        self.rodadaAtual = Rodada(self.turnId)
        self.rodadaAtual.atualizarOrdem(self.jogadores)
        self.turnId += 1
        self.rodadas.append(self.rodadaAtual)

    def jogar(self):
        # Função principal para o loop do jogo
        self.currentPlayerid = 0
        self.currentPlayer = self.jogadores[self.currentPlayerid]
        self.turnId = 0
        self.criaRodada()

        # GAME LOOP
        while True:
            # Desenha os gráficos do jogo
            self.draw_graphics()

            self.currentPlayer = self.rodadaAtual.turnos[self.currentPlayerid].getJogador(
            )

            # Processa os eventos do Pygame
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.currentPlayer.controlador.awaitsInput():
                        if event.button == 1 and not self.locked:
                            self.fazerTurnoJogador(event)
                    elif not self.locked:  # Ainda espera um clique para passar o turno da IA
                        self.fazerTurnoJogador(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Verifica se o jogador atual tem suprimentos negativos e transforma em zumbi
            if self.currentPlayer.suprimentos < 0:
                self.currentPlayer.transforma_zumbi()

            # Verifica quantos jogadores ativos restam no jogo
            jogadores_ativos = [j for j in self.jogadores if not j.isZombie()]
            if len(jogadores_ativos) == 1:
                if self.exibir_tela_final(jogadores_ativos[0], "assets/Background.jpg"):
                    self.__init__(self.screen, self.qtd_jogadores)
                else:
                    pygame.quit()
                    sys.exit()

            # Atualiza a tela do jogo
            pygame.display.update()

    def fazerTurnoJogador(self, event):
        # Rola os dados para o turno do jogador
        roll = sprite_dado.rolar()
        roll += sprite_dado2.rolar()
        self.tabuleiro.iterarCasas(self.currentPlayer, roll)

        # Passa o turno para o próximo jogador
        self.currentPlayerid += 1
        if self.currentPlayerid > len(self.rodadaAtual.turnos) - 1:
            self.currentPlayerid = 0
            self.criaRodada()

    def exibir_tela_final(self, jogador_vencedor, caminho_imagem_fundo):
        # Carrega a imagem de fundo
        # imagem_fundo = pygame.image.load(caminho_imagem_fundo)
        imagem_fundo = pygame.image.load("assets/GigaChadMonopoly.webp")

        pygame.mixer.init()

        pygame.mixer.music.load("assets/Can you feel my heart.mpeg")

        # pygame.mixer.music.set_volume()

        pygame.mixer.music.play()

        # Obtém o tamanho da tela
        tamanho_tela = self.screen.get_size()

        # Redimensiona a imagem de fundo para o tamanho da tela
        imagem_fundo = pygame.transform.scale(imagem_fundo, tamanho_tela)

        # Desenha a imagem de fundo
        self.screen.blit(imagem_fundo, (0, 0))

        # Exibe a mensagem de vitória
        fonte_vencedor = get_fonte_titulo(80)
        texto_vencedor = fonte_vencedor.render(
            f'Jogador {(jogador_vencedor.id)+1} Sobreviveu!', True, (255, 255, 255))
        self.screen.blit(texto_vencedor, (350, 300))

        # Desenha o botão de "Sair"
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

    def draw_graphics(self):
        # Desenha o fundo do tabuleiro na tela
        self.screen.blit(self.BGTABULEIRO, (0, 0))
        # Desenha os peões na tela do jogo
        for jogador in self.jogadores:
            jsprite = jogador.peca.jogadorSprite
            self.screen.blit(jsprite.imagem, jsprite.rect)

        # Desenha o dinheiro dos jogadores
        for jogador in self.jogadores:
            if jogador.id != self.currentPlayerid:
                jogador.renderizar_suprimento(
                    self.font, self.screen, (0, 0, 0))
            else:
                jogador.renderizar_suprimento(
                    self.font, self.screen, (97, 19, 11))

        # Exibe informações das casas do tabuleiro
        self.tabuleiro.exibir_info_casa(self.screen)
        self.dlog.displayLog()

        # Desenha os dados na tela
        sprite_dado.draw(self.screen)
        sprite_dado2.draw(self.screen)

        # Desenha o baralho na tela
        self.baralhoInstance.draw(self.screen)

        # Atualiza a tela do jogo
        pygame.display.update()

    def iniciar_jogadores(self, qtd_jogadores, casaInicial, qtd_ia, dificuldadeIA=1):
        # Define as informações dos peões (imagens e posições)
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

        # Cria a lista de controladores para os jogadores (humanos ou IA)
        controladores = []
        for i in range(0, qtd_jogadores):
            if i < qtd_ia:
                controladores.append(IA(dificuldadeIA, self))
            else:
                controladores.append(Humano(self))

        # Define as posições iniciais dos jogadores
        self.posicoes_iniciais = [(baseCoordX, baseCoordY),
                                  (baseCoordX + xDeviation,
                                   baseCoordY + yDeviation),
                                  (baseCoordX - xDeviation,
                                   baseCoordY - yDeviation),
                                  (baseCoordX + xDeviation,
                                   baseCoordY + yDeviation),
                                  (baseCoordX, baseCoordY - yDeviation),
                                  # Posições iniciais para cada jogador
                                  (baseCoordX - xDeviation, baseCoordY)]

        # Cria os jogadores e adiciona à lista de jogadores
        for i in range(qtd_jogadores):
            jogador = Jogador(controladores[len(controladores) - i - 1], i, casaInicial,
                              JogadorSprite(
                                  peao_info[i][0], peao_info[i][2], self.posicoes_iniciais[i]),
                              self.tabuleiro)
            self.jogadores.append(jogador)

    def lock(self):
        # Trava o jogo (não permite ações dos jogadores)
        self.draw_graphics()
        self.locked = True

    def unlock(self):
        # Destrava o jogo (permite ações dos jogadores)
        self.locked = False
