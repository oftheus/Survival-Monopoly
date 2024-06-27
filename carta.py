import pygame
from utilitario import *
import random

class Carta:
    def __init__(self, id):
        self.id = id
    
    def aplicarEfeito(self, jogador):
        return