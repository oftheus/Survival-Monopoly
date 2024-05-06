import pygame
from utilitario import *
import random

class Carta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagem_capa = get_cartacapa() # Carrega a imagem da capa da carta
        self.imagens_cartas = list(range(1, 21)) # Lista com os números das 20 cartas
        self.image = self.imagem_capa
        self.rect = self.image.get_rect()
        self.rect.center = (250, 550) # Posição da carta na tela do jogo
        self.mostrando_capa = True
        self.cartas_selecionadas = [] # Lista para armazenar os números das cartas já selecionadas

    # Método para trocar a carta exibida
    def trocar_carta(self):
        if self.mostrando_capa:
             # Se a carta exibida for a capa, seleciona uma carta aleatória não selecionada
            cartas_disponiveis = list(set(self.imagens_cartas) - set(self.cartas_selecionadas))
            if cartas_disponiveis: # Verifica se ainda há cartas disponíveis
                numero_carta = random.choice(cartas_disponiveis)
                self.cartas_selecionadas.append(numero_carta) # Adiciona a carta selecionada à lista de cartas selecionadas
                self.image = get_carta(numero_carta) # Carrega a imagem correspondente ao número da carta
                self.mostrando_capa = False # Muda para mostrar a carta selecionada
        else:
            self.image = self.imagem_capa # Mostra a capa da carta
            self.mostrando_capa = True # Muda para mostrar a capa novamente

    def draw(self, screen):
        # Método para desenhar a carta na tela
        screen.blit(self.image, self.rect)
