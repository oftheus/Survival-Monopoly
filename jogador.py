import pygame
from utilitario import *
from tela_qtd_jogadores import*


class Jogador:
    def __init__(self, id_jogador):
        self.id = id_jogador
        self.suprimentos = 1500  # Quantidade inicial de "dinheiro" para cada jogador
        self.posicao = 0  # Posição inicial no tabuleiro
        self.imagem = pygame.image.load(f"assets/peao{id_jogador + 1}.png").convert_alpha()  # Carrega a imagem do jogador
        self.imagem = pygame.transform.scale(self.imagem, (28, 30))  # Redimensiona a imagem

    def renderizar_suprimento(self, font, screen):
        # Renderiza o formato de fundo
        suprimento_bg_rect = pygame.Rect(200 + self.id * 150, 200, 80, 30)
        pygame.draw.rect(screen, (((184,219,211))), suprimento_bg_rect, border_radius=15)  # Retângulo arredondado

        screen.blit(self.imagem, (200 + self.id * 148, 200))  # Ajusta a posição com base no id do jogador
        texto_suprimento = font.render(f"{self.suprimentos}", True, (0,0,0))
        screen.blit(texto_suprimento, (230 + self.id * 150, 202))  # Ajusta a posição com base no id do jogador





class Peao(pygame.sprite.Sprite):
    def __init__(self, jogador, posicao_inicial):
        super().__init__()
        self.jogador = jogador
        self.imagem = pygame.image.load(self.jogador.image_path).convert_alpha()  # Carrega a imagem do peão do jogador
        self.imagem = pygame.transform.scale(self.imagem, self.jogador.size)  # Redimensiona a imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = posicao_inicial  # Define a posição inicial


def iniciar_jogadores(qtd_jogadores):
    peao_info = [("assets/peao1.png", (8, 670), (40, 45)), # (x,y) , (largura, altura)
                 ("assets/peao2.png", (58, 670), (40, 49)),
                 ("assets/peao3.png", (108, 670), (40, 40)),
                 ("assets/peao4.png", (8, 750), (40, 28)),
                 ("assets/peao5.png", (58, 750), (40, 33)),
                 ("assets/peao6.png", (108, 740), (40, 49))]

    posicoes_iniciais = [(8, 670), (58, 670), (108, 670), (8, 750), (58, 750), (108, 740)]  # Posições iniciais para cada jogador
    jogadores = []
    for i in range(qtd_jogadores):
        jogador = Jogador(i)
        # Atribui o caminho da imagem do peão e o tamanho com base em peao_info
        jogador.image_path, _, jogador.size = peao_info[i]
        jogadores.append(jogador)
    return jogadores, posicoes_iniciais