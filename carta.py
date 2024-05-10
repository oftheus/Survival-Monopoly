import pygame
from utilitario import *

class Carta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagem_capa = get_cartacapa() # Carrega a imagem da capa da carta
        self.image = self.imagem_capa
        self.rect = self.image.get_rect()
        self.rect.center = (250, 550) # Posição da carta na tela do jogo

    def draw(self, screen):
        # Método para desenhar a carta na tela
        screen.blit(self.image, self.rect)
