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
        for i in range(1,19):
            if i+1 != 14:
                newCarta = CartaDinheiro(i+1,self.custosCartas[i-1])
            else:
                newCarta = CartaDistracao(i+1)
            self.cartas.append(newCarta)
        self.cartas.append(CartaTeletransporte(i+2))
        #verifica se cartas estão corretas
        for carta in self.cartas:
            carta.printSelf()

    # Método para trocar a carta exibida
    def sorteia(self):
        if self.mostrando_capa:
            self.mostrando_capa = False  # Muda para mostrar a carta selecionada
            numero_carta = random.randint(2,21)
            self.image = get_carta_sprite(numero_carta)
            self.image = pygame.transform.smoothscale(self.image, (140,200))
            return self.searchCard(numero_carta)
        else:
            self.image = self.imagem_capa  # Mostra a capa da carta
            self.image = pygame.transform.smoothscale(self.image, (140,200))
            self.mostrando_capa = True  # Muda para mostrar a capa novamente
            return 0
        
    def draw(self, screen):
        # Método para desenhar a carta na tela
        screen.blit(self.image, self.rect)

    def searchCard(self, cardId):
        for carta in self.cartas:
            if carta.id == cardId:
                return carta
        return self.cartas[2]