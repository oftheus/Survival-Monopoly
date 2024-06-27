import pygame
from utilitario import *
import random
from carta import*

class CartaTeletransporte(Carta):
    def __init__(self, id):
        self.id = id

    def aplicarEfeito(self, jogador):
        jogador.encurrala()