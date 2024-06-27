import pygame
from utilitario import *
import random
from carta import *
from cartaDinheiro import *
from cartaDistracao import *
from cartaTeletransporte import *

class Baralho(pygame.sprite.Sprite):
    _instance = None  # Singleton

    @classmethod
    def instance(cls):
        # Método de classe para garantir que apenas uma instância de Baralho seja criada (Singleton)
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def init(self):
        # Inicializa a classe base
        super().__init__()
        self.imagem_capa = get_cartacapa()  # Carrega a imagem da capa da carta
        # Lista com os números das 20 cartas
        self.imagens_cartas = list(range(1, 21))
        self.image = self.imagem_capa
        self.rect = self.image.get_rect()
        self.rect.center = (240, 510)  # Posição da carta na tela do jogo
        self.mostrando_capa = True  # Indica se a capa da carta está sendo mostrada
        self.image = pygame.transform.smoothscale(self.image, (140, 200))  # Redimensiona a imagem da carta

        # Lista para armazenar os números das cartas já selecionadas
        self.cartas_selecionadas = []
        # Custos associados a cada carta
        self.custosCartas = [100, 150, 50, 40, 120, 75, 25, 40, 80, -20, -40, -20, -40, -25, -200, -100, -150, -50]
        self.cartas = []  # Lista para armazenar as cartas
        self.cartaAtual = None  # Carta atualmente exibida
        self.criaCartas()  # Cria as cartas do baralho

    def criaCartas(self):
        # Método para criar as cartas
        for i in range(1, 19):
            if i + 1 != 14:
                newCarta = CartaDinheiro(i + 1, self.custosCartas[i - 1])
            else:
                newCarta = CartaDistracao(i + 1)
            self.cartas.append(newCarta)
        self.cartas.append(CartaTeletransporte(i + 2))
        
        # Verifica se as cartas estão corretas
        for carta in self.cartas:
            carta.printSelf()

    def sorteia(self):
        # Método para trocar a carta exibida
        if self.mostrando_capa:
            self.mostrando_capa = False  # Muda para mostrar a carta selecionada
            numero_carta = random.randint(2, 21)
            self.image = get_carta_sprite(numero_carta)
            self.image = pygame.transform.smoothscale(self.image, (140, 200))
            return self.searchCard(numero_carta)
        else:
            self.image = self.imagem_capa  # Mostra a capa da carta
            self.image = pygame.transform.smoothscale(self.image, (140, 200))
            self.mostrando_capa = True  # Muda para mostrar a capa novamente
            return 0
        
    def draw(self, screen):
        # Método para desenhar a carta na tela
        screen.blit(self.image, self.rect)

    def searchCard(self, cardId):
        # Método para buscar uma carta pelo seu ID
        for carta in self.cartas:
            if carta.id == cardId:
                return carta
        return self.cartas[2]
