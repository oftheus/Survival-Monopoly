import pygame
from utilitario import *
import random
from carta import*

class CartaDinheiro(Carta):
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor

    def aplicarEfeito(self, jogador):
        jogador.modificarSuprimentos(self.valor)