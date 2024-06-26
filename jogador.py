import pygame
from utilitario import *
from tela_qtd_jogadores import *
from peca import *


class Jogador:
    def __init__(self, id_jogador, pos_inicial, jogadorSprite):
        self.id = id_jogador
        self.pos_inicial = pos_inicial
        self.suprimentos = 1500  # Quantidade inicial de "dinheiro" para cada jogador
        self.imagem = pygame.image.load(
            # Carrega a imagem do jogador
            f"assets/peao{id_jogador + 1}.png").convert_alpha()
        self.imagem = pygame.transform.scale(
            self.imagem, (28, 30))  # Redimensiona a imagem
        self.peca = Peca(self.pos_inicial, jogadorSprite)
        self.estadoZumbi = False  # mudar depois!

        #inicia titulos de assentamento

    def renderizar_suprimento(self, font, screen):
        # Renderiza o formato de fundo
        suprimento_bg_rect = pygame.Rect(200 + self.id * 150, 200, 80, 30)
        pygame.draw.rect(screen, (((184, 219, 211))), suprimento_bg_rect,
                         border_radius=15)  # Retângulo arredondado

        # Ajusta a posição com base no id do jogador
        screen.blit(self.imagem, (200 + self.id * 148, 200))
        if not self.isZombie():
            texto_suprimento = font.render(
                f"{self.suprimentos}", True, (0, 0, 0))
        else:
            texto_suprimento = font.render("Morto", True, (0, 0, 0))
        # Ajusta a posição com base no id do jogador
        screen.blit(texto_suprimento, (230 + self.id * 150, 202))

    def transforma_zumbi(self):
        self.peca.jogadorSprite = JogadorSprite(
            "assets/zumbi.png", (55, 80),  (50, 700))
        self.peca.casa = self.pos_inicial
        self.estadoZumbi = True
        # print("zumbi!")
        # print(self.peca.jogadorSprite.image)
        # algo com state ou outro modo de implementar

    def isZombie(self):
        return self.estadoZumbi


class JogadorSprite(pygame.sprite.Sprite):
    def __init__(self, imagePath, size, posicao_inicial):
        super().__init__()
        # Carrega a imagem do peão do jogador
        self.imagem = pygame.image.load(imagePath).convert_alpha()
        self.imagem = pygame.transform.scale(
            self.imagem, size)  # Redimensiona a imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = posicao_inicial  # Define a posição inicial
