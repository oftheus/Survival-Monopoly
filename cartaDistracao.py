import pygame
from utilitario import *
import random
from carta import*

class CartaDistracao(Carta):
    def __init__(self, id):
        self.id = id

    def aplicarEfeito(self, jogador):
        jogador.ganharCartaEscape()