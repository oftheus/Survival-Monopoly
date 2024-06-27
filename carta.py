import pygame
from utilitario import *
import random

class Carta:
    #Funções de cada subclasse de carta implementadas através de polimorfismo
    def __init__(self, id):
        self.id = id
    
    def aplicarEfeito(self, jogador):
        return
    
    def printSelf(self):
        print(self.id)