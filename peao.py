import pygame
from utilitario import *
from tela_qtd_jogadores import*

class Peao(pygame.sprite.Sprite):
    def __init__(self, caminho_imagem, posicao, tamanho):
        super().__init__()
        self.image = pygame.image.load(caminho_imagem).convert_alpha()  # Carrega a imagem do peão
        self.image = pygame.transform.scale(self.image, tamanho)  # Redimensiona a imagem para o tamanho de cada imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = posicao

def iniciar_peoes(qtd_jogadores):
    peao_info = [("assets/peao1.png", (8, 670), (40, 45)),  # (caminho da imagem, posição na tela, tamanho da imagem)
                 ("assets/peao2.png", (58, 670), (40, 49)),
                 ("assets/peao3.png", (108, 670), (40, 40)),
                 ("assets/peao4.png", (8, 750), (40, 28)),
                 ("assets/peao5.png", (58, 750), (40, 33)),
                 ("assets/peao6.png", (108, 740), (40, 49))]
    peoes = [] # Lista para armazenar os objetos peão
    for info in peao_info[:qtd_jogadores]: # Para cada conjunto de informações de peão no número especificado de jogadores
        peoes.append(Peao(*info)) # Adiciona um novo objeto peão à lista, usando as informações fornecidas
    return peoes # Retorna a lista de objetos peão criados