import pygame
from utilitario import *
import random
from carta import *
from cartaDinheiro import *
from cartaDistracao import *
from cartaTeletransporte import *

class Baralho(pygame.sprite.Sprite):
    
    _instance = None #Singleton

    @classmethod #copiei da internet
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


    def init(self):
        super().__init__()
        self.imagem_capa = get_cartacapa()  # Carrega a imagem da capa da carta
        # Lista com os números das 20 cartas
        self.imagens_cartas = list(range(1, 21))
        self.image = self.imagem_capa
        self.rect = self.image.get_rect()
        self.rect.center = (240, 510)  # Posição da carta na tela do jogo
        self.mostrando_capa = True
        self.image = pygame.transform.smoothscale(self.image, (140,200))

        # Lista para armazenar os números das cartas já selecionadas
        self.cartas_selecionadas = []
        self.custosCartas = [100,150,50,40,120,75,25,40,80,-20,-40,-20,-40,-25,-200,-100,-150,-50]
        self.cartas = []
        self.cartaAtual = None
        self.criaCartas()

    def criaCartas(self):
        for i in range(1,len(self.imagens_cartas)):
            print(i)
            if i ==18:
                newCarta = CartaDistracao(i)
            elif i ==19:
                newCarta = CartaTeletransporte(i)
            else:
                newCarta = CartaDinheiro(i,self.custosCartas[i])
            self.cartas.append(newCarta)

    # Método para trocar a carta exibida
    def sorteia(self):
        if self.mostrando_capa:
            # Se a carta exibida for a capa, seleciona uma carta aleatória não selecionada
            cartas_disponiveis = list(
                set(self.imagens_cartas) - set(self.cartas_selecionadas))
            if cartas_disponiveis:  # Verifica se ainda há cartas disponíveis
                numero_carta = random.choice(cartas_disponiveis)
                # Adiciona a carta selecionada à lista de cartas selecionadas
                self.cartas_selecionadas.append(numero_carta)
                # Carrega a imagem correspondente ao número da carta
                self.image = get_carta(numero_carta)
                self.image = pygame.transform.smoothscale(self.image, (140,200))
                self.mostrando_capa = False  # Muda para mostrar a carta selecionada
                return self.cartas[numero_carta % len(self.cartas)]
        else:
            self.image = self.imagem_capa  # Mostra a capa da carta
            self.image = pygame.transform.smoothscale(self.image, (140,200))
            self.mostrando_capa = True  # Muda para mostrar a capa novamente
            return 0
    def draw(self, screen):
        # Método para desenhar a carta na tela
        screen.blit(self.image, self.rect)